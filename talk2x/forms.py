from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.forms import ModelForm
from .models import FutureLunch

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name', 'meaning_of_life']
        help_texts = {
            'email': None,
            'password1': None,
            'password2': None
        }

class EditProfile(ModelForm):

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'meaning_of_life']

class FutureLunchForm(ModelForm):

    class Meta:
        model = FutureLunch
        fields = ['date']

#code taken from: https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
