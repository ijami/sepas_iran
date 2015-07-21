__author__ = 'Ehsan'
from django.shortcuts import render, redirect
from tourist.forms import MyUserCreationForm


def register(request):
    if not request.POST:
        form = MyUserCreationForm()
        return render(request, 'tourist/register.html', {
            'form': form
        })

    form = MyUserCreationForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'tourist/register.html', {
        'form': form
    })
