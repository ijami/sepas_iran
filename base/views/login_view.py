from base.forms import LoginForm

__author__ = 'Iman'

from django.contrib.auth import logout, login, authenticate
from django.shortcuts import redirect, render
from django.core.urlresolvers import reverse


def logout_user(request):
    logout(request)
    return redirect(reverse('home'))


def login_user(request):
    print("salam")
    if request.user.is_authenticated():
        return redirect(reverse('home'))

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                return redirect("home")
        else:
            return render(request, 'base/login.html', {'errors': ["نام کابری یا گذرواژه اشتباه است"]})

    return render(request, 'base/login.html')
