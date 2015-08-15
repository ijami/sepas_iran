__author__ = 'MJR'
from django.shortcuts import render, redirect
from django.conf import settings


def panel(request):
    return render(request, 'service_provider/panel.html', {'site_url': settings.SITE_URL})

