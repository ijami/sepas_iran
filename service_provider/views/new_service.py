__author__ = 'MJR'
from django.shortcuts import render, redirect
from service.forms import RoomForm, FlightForm, TourForm
from django.core.urlresolvers import reverse


def new_service(request):
    user = request.user.site_user
    if request.method == 'GET':
            if user:
                if user.get_fields()['type'] != 'tourist':
                    t = user.get_fields()['type']
                    if t == 'hotel':
                        C = RoomForm
                    elif t == 'agency':
                        C = TourForm
                    else:
                        C = FlightForm
                    form = C()
                    return render(request, 'service_provider/add_service.html', {'form': form, 'type': t})
    elif request.method == 'POST':
        form = TourForm(request.POST, request.FILES)
        print("golabi")
        print(form.errors)
        print(form.is_valid())
        if form.is_valid():
            print("bordim")
            form.save(user=user)
        return redirect(reverse('service_provider_panel'))


