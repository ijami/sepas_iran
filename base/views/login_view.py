__author__ = 'Iman'

from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.core.urlresolvers import reverse


def logout_user(request):
    logout(request)
    return redirect(reverse('home'))


def login_user(request):
    if request.method == 'POST':
        pass
    return render(request, 'base/login.html')
