__author__ = 'Ehsan'
from django.shortcuts import render

def register(request):
    return render(request, 'tourist/register.html')
