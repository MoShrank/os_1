from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from .forms import *
from django.urls import reverse

from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import FutureLunch, User, Lunch
from .decorators import *

from .tasks import send_email_task

from django.contrib.sites.shortcuts import get_current_site
from .tokens import account_activation_token

from django.shortcuts import get_object_or_404

from django.contrib.auth import views as auth_views

from datetime import date

profile_decorator = [ login_required, users_profile ]
lunch_decorator = [ login_required, profile_complete ]

# Create your views here.


@login_required
def home(request):

    todaysLunch = None

    fl = FutureLunch.objects.filter(user=request.user)

    try:
        todaysLunch = FutureLunch.objects.get(date=date.today())
    except Exception as e:
        pass
    pl = Lunch.objects.filter(user=request.user)
    if todaysLunch is not None:
        fl = pl.exclude(id=todaysLunch.id)


    context = { 'FutureLunch' : fl, 'PastLunch' : pl, 'todaysLunch' : todaysLunch }

    return render(request, 'home.html', context)


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def tc(request):
    return render(request, 'tc.html')


class Signup(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = '/activate'

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

        send_email_task.delay('confirm registration', email, { 'name' : user.first_name, 'link' : link })
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
        return HttpResponseRedirect(reverse('profile_edit', kwargs={'pk' : str(request.user.pk), 'slug' : request.user.slug}))
    else:
        return HttpResponse('Activation link is invalid!')

    # code for activating email taken and modified from https://medium.com/@frfahim/django-registration-with-confirmation-email-bb5da011e4ef


def activation_email(request):

    if request.method == 'GET':

        return render(request, 'registration/activation_email.html', {'form' : ActivationForm})

    elif request.method == 'POST':

        email = request.POST.get('email')
        user = get_object_or_404(User, email=email)
        if user.is_active == True:
            return HttpResponse('already active')
        pk = user.pk

        link = get_current_site(request).domain + reverse('activate', kwargs={'pk' : str(pk), 'token' : str(account_activation_token.make_token(user))})

        send_email_task.delay('confirm registration', email, { 'name' : user.first_name, 'link' : link })

        return HttpResponseRedirect(reverse('activate_page'))


@method_decorator(lunch_decorator, name='dispatch')
class CreateFutureLunch(CreateView):
    form_class = FutureLunchForm
    template_name = 'lunch.html'

    def get_success_url(self):
        return reverse('lunch')

    def form_valid(self, form):

        form.instance.user = self.request.user
        if self.request.user.subscribe_to_email:
            send_email_task.delay('confirm lunch', self.request.user.email, { 'user' : self.request.user, 'date' : form.instance.date })
        return super().form_valid(form)


@method_decorator(profile_decorator, name='dispatch')
class EditProfile(UpdateView):
    model = User
    form_class = EditProfile
    template_name = 'profile_edit.html'
    pk_url_kwarg = 'user_id'

    def get_success_url(self):
        return reverse('profile', kwargs={'slug' : self.object.slug, 'user_id' : self.object.id})


@method_decorator(profile_decorator, name='dispatch')
class Profile(DetailView):
    template_name = 'profile.html'
    model = User
    query_pk_and_slug  = True
    pk_url_kwarg = 'user_id'
    context_object_name = 'user'


def activate_page(request):
    return render(request, 'registration/activate_email.html')


@login_required
@user_is_lunch_author
def cancel_lunch(request, lunch_id):

    FutureLunch.objects.get(id=lunch_id).delete()

    return HttpResponseRedirect(reverse('profile', kwargs={'slug' : request.user.slug, 'user_id' : request.user.id}))

@login_required
def unsubscribe(request, slug, user_id):

    user = request.user
    user.subscribe_to_email = False
    user.save()

    return HttpResponseRedirect(reverse('profile', kwargs={'slug' : slug, 'user_id' : user.id}))

@login_required
def subscribe(request, slug, user_id):

    user = request.user
    user.subscribe_to_email = True
    user.save()

    return HttpResponseRedirect(reverse('profile', kwargs={'slug' : slug, 'user_id' : user.id}))


#class ResetRedirect(auth_views.PasswordResetConfirmView):
#    pass
    #def get(self, request):

    #    return HttpResponseRedirect('/')
