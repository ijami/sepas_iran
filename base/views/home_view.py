__author__ = 'Javad'
from django.shortcuts import render
from django.contrib.auth import authenticate, login


def home(request):
    return render(request, 'base/home.html')
