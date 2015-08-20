from setuptools.compat import unicode

__author__ = 'Ehsan'
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from service_provider.forms import ServiceProviderCreationForm


def register(request):
    if request.method != "POST":
        form = ServiceProviderCreationForm()
        return render(request, 'service_provider/register.html', {
            'form': form
        })

    # print(request.POST)
    form = ServiceProviderCreationForm(request.POST, request.FILES)
    # print(unicode(form['username'].value()).encode('utf8'))

    if form.is_valid():
        form.save()
        return redirect(reverse('login'))

    return render(request, 'service_provider/register.html', {
        'form': form
    })
