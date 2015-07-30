__author__ = 'Javad'
from django.shortcuts import render
from django.contrib.auth import authenticate, login


def home(request):
    if request.POST:

        user = authenticate(username="ehsan", password="ehsanehsan")
        login(request, user)

    return render(request, 'base/home.html')
