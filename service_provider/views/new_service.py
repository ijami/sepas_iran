from http.client import HTTPResponse

__author__ = 'MJR'
from django.shortcuts import render, redirect
from service.forms import RoomForm, FlightForm, TourForm
from django.core.urlresolvers import reverse
from base.views.decorators import service_provider_required

@service_provider_required()
def new_service(request):
    C = None
    user = request.user.site_user
    if not user.is_active:
        return render(request, 'service_provider/inactive_user_error.html')
    if request.method == 'GET':
            if user:
                if user.get_fields()['type'] != 'tourist':
                    t = user.get_fields()['type']
                    if t == 'agency':
                        C = TourForm
                    elif t == 'hotel':
                        C = RoomForm
                    else:
                        C = FlightForm
                    form = C()
                    return render(request, 'service_provider/add_service.html', {'form': form, 'type': t})
    elif request.method == 'POST':
        if user:
                if user.get_fields()['type'] != 'tourist':
                    t = user.get_fields()['type']
                    if t == 'agency':
                        C = TourForm
                    elif t == 'hotel':
                        C = RoomForm
                    else:
                        C = FlightForm
                    form = C(request.POST, request.FILES)
                    if form.is_valid():
                        form.save(user=user)
                        return redirect(reverse('service_provider_panel'))
                    return render(request, 'service_provider/add_service.html', {'form': form, 'type': user.get_fields()['type']})

