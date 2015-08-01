__author__ = 'Javad'
from django.shortcuts import render
from django.contrib.auth import authenticate, login


def home(request):
    user = authenticate(username="arman", password="salam")
    login(request, user)

    return render(request, 'base/home.html')
