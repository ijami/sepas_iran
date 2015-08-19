__author__ = 'Mohsen'
from django.shortcuts import render
from service.models import Service, Tour

def home(request):
    new_services = Service.objects.all()[0:5]


    return render(request, 'base/home.html',{
        'new_services': new_services
    })
