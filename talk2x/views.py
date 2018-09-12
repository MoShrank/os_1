from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from .forms import *
from .send_email import sendemail
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.core.exceptions import ValidationError
from .models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.


def home(request):
    return render(request, 'home.html');


def contact(request):
    return render(request, 'contact.html')

class Signup(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = '/'

    def form_valid(self, form):

        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        user = authenticate(email=email, password=password)
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')

        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class FutureLunch(CreateView):
    form_class = FutureLunch
    template_name = 'lunch.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class EditProfile(UpdateView):
    model = User
    template_name = 'profile_edit.html'
    form_class = SignUpForm
    pk_url_kwarg = 'user_id'
    success_url = '/profile/{user_id}-{slug}'

@method_decorator(login_required, name='dispatch')
class Profile(DetailView):
    template_name = 'profile.html'
    model = User
    query_pk_and_slug  = True
    pk_url_kwarg = 'user_id'
