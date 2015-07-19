__author__ = 'Javad'
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse

def home(request):
    return render(request, 'home.html')