from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.forms import ModelForm
from .models import FutureLunch

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid code email addres.')

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name', 'meaning_of_life')

class FutureLunch(ModelForm):

    class Meta:
        model = FutureLunch
        fields = ['date']
