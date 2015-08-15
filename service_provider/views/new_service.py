__author__ = 'MJR'
from django.shortcuts import render, redirect
from django.conf import settings
from django.template import RequestContext
from service.forms import RoomForm, FlightForm, TourForm


def new_service(request):
    user = request.user.site_user
    if user:
        if user.get_fields()['type'] != 'tourist':
            t = user.get_fields()['type']
            if t == 'hotel':
                C = RoomForm
            elif t == 'agency':
                C = TourForm
            else:
                C = FlightForm
            form = C(user)
            return render(request, 'add_service.html', {'form': form, 'type': t})