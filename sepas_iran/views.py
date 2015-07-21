__author__ = 'Javad'
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from tourist.forms import MyUserCreationForm
from django.contrib.auth import authenticate, login, logout


def home(request):
    if request.POST:

        user = authenticate(username="ehsan", password="ehsanehsan")
        login(request, user)

    return render(request, 'home.html')
