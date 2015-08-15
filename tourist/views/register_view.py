from setuptools.compat import unicode

__author__ = 'Ehsan'
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from tourist.forms import TouristCreationForm


def register(request):
    if request.method != "POST":
        form = TouristCreationForm()
        return render(request, 'tourist/register.html', {
            'form': form
        })

    form = TouristCreationForm(request.POST)
    print(unicode(form['username'].value()).encode('utf8'))

    if form.is_valid():
        form.save()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect(reverse('home'))

    return render(request, 'tourist/register.html', {
        'form': form
    })
