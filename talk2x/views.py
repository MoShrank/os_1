from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from .forms import *
from django.urls import reverse

from django.contrib.auth import login, authenticate
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import FutureLunch, User, Lunch
from .decorators import *

from .send_email import send_email

from django.contrib.sites.shortcuts import get_current_site
from .tokens import account_activation_token

# Create your views here.


def home(request):

    if request.user.is_authenticated:

        fl = FutureLunch.objects.filter(user=request.user)
        pl = Lunch.objects.filter(user=request.user)

        context = { 'FutureLunch' : fl, 'PastLunch' : pl }

        return render(request, 'home.html', context)

    return render(request, 'home.html');


def contact(request):
    return render(request, 'contact.html')


class Signup(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = '/'

    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
        else:
            return render(request, self.template_name, { 'form' : self.form_class})

    def form_valid(self, form):

        email = form.cleaned_data.get('email')

        user = form.save(commit=False)
        user.is_active = False
        user.save()

        link = get_current_site(self.request).domain + reverse('activate', kwargs={'pk' : str(user.pk), 'token' : str(account_activation_token.make_token(user))})

        send_email('confirm registration', email, { 'name' : user.first_name, 'link' : link })

        return super().form_valid(form)


def activate(request, pk, token):

    try:
        user = User.objects.get(pk=pk)
    except Exception as e:
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return HttpResponseRedirect('/')
    else:
        return HttpResponse('Activation link is invalid!')

    # code for activating email taken and modified from https://medium.com/@frfahim/django-registration-with-confirmation-email-bb5da011e4ef


@method_decorator(login_required, name='dispatch')
class CreateFutureLunch(CreateView):
    form_class = FutureLunchForm
    template_name = 'lunch.html'

    def get_success_url(self):
        return reverse('lunch')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class EditProfile(UpdateView):
    model = User
    form_class = EditProfile
    template_name = 'profile_edit.html'
    pk_url_kwarg = 'user_id'

    def get_success_url(self):
        return reverse('profile', kwargs={'slug' : self.object.slug, 'user_id' : self.object.id})


@method_decorator(login_required, name='dispatch')
class Profile(DetailView):
    template_name = 'profile.html'
    model = User
    query_pk_and_slug  = True
    pk_url_kwarg = 'user_id'


@login_required
@user_is_lunch_author
def cancel_lunch(request, lunch_id):

    FutureLunch.objects.get(id=lunch_id).delete()

    return HttpResponseRedirect(reverse('profile', kwargs={'slug' : request.user.slug, 'user_id' : request.user.id}))
