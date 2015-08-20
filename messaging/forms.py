__author__ = 'Mohsen'

from django import forms
from base.models import SiteUser
from django.forms.models import ModelForm
from messaging.models import Message

class NewMessageForm(forms.Form):
    receiver = forms.ModelChoiceField(queryset=SiteUser.objects.exclude())
    header = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'type':'text', 'style':'margin-bottom: 5px;', 'placeholder':'عنوان پیام'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'پیام خود را وارد کنید', 'style':'height: 215px;'}))
