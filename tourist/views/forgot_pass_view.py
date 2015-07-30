__author__ = 'Ehsan'
from django.shortcuts import render

def forgot_pass(request):
    return render(request, 'tourist/forgot_pass.html')