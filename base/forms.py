from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.forms.forms import Form

__author__ = 'Ehsan'

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254, label="", widget=forms.TextInput(attrs={'placeholder': ""}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'placeholder': ""}))

    error_messages = {
        'invalid_login': "نام کاربری یا گذرواژه اشتباه است",
        'inactive': "این کاربر غیر فعال است",
    }
    #pass
