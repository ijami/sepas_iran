__author__ = 'Ehsan'
from django.shortcuts import render, redirect
from tourist.forms import MyUserCreationForm
from django.contrib.auth import authenticate, login, logout


def register(request):
    if not request.POST:
        form = MyUserCreationForm()
        return render(request, 'tourist/register.html', {
            'form': form
        })

    form = MyUserCreationForm(request.POST)

    if form.is_valid():
        form.save()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/')

    return render(request, 'tourist/register.html', {
        'form': form
    })
