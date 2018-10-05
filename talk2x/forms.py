from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.forms import ModelForm
from .models import FutureLunch
from .validators import validate_code_mail

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'accepted_tc']
        labels = {
            'accepted_tc' : 'accept terms and conditions'
        }


class ActivationForm(forms.Form):

    email = forms.EmailField(label='email', max_length=50, validators=[validate_code_mail])


class EditProfile(ModelForm):

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'meaning_of_life', 'picture', 'subscribe_to_email']


class FutureLunchForm(ModelForm):

    class Meta:
        model = FutureLunch
        fields = ['date']

#code taken from: https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
