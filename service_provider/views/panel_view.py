__author__ = 'MJR'
from django.shortcuts import render, redirect



def panel(request):
    return render(request, 'provider_dashbord_base.html', {})

