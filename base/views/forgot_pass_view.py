__author__ = 'Ehsan'
from django.shortcuts import render


def forgot_pass(request):
    return render(request, 'base/forgot_pass.html')
