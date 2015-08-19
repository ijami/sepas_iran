__author__ = 'Mohsen'

from django import forms
from django.forms.models import ModelForm
from messaging.models import Message

class new_message_form(forms.Form):
    class Meta:
        model = Message
        fields = ['receiver', 'text', 'header']
