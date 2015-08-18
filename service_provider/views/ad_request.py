__author__ = 'MJR'
from django.shortcuts import render, redirect
from service.forms import RoomForm, FlightForm, TourForm
from django.core.urlresolvers import reverse


def advertisement_request(request):
    return render(request, 'service_provider/advertisement_request.html')