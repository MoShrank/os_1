from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.forms import ModelForm
from .models import FutureLunch
from .validators import validate_code_mail
from . import widgets

class SignUpForm(UserCreationForm):


    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']



class ActivationForm(forms.Form):

    email = forms.EmailField(label='email', max_length=50, validators=[validate_code_mail])


class EditProfile(ModelForm):

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'meaning_of_life', 'subscribe_to_email']


class FutureLunchForm(ModelForm):

    date = forms.CharField(
        widget = widgets.DateInput,

        )

    class Meta:
        model = FutureLunch
        fields = ['date']
