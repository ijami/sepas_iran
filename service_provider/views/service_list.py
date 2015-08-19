__author__ = 'MJR'
from django.shortcuts import render, redirect
from service.models import Tour, Room, Flight, Service
from service.forms import CapacityAddingForm
import datetime
from django.core.urlresolvers import reverse
from base.views.decorators import service_provider_required

@service_provider_required()
def service_list(request):
    user = request.user.site_user
    type = user.get_fields()['type']
    service = []
    if type != 'tourist':
        if type == 'hotel':
            q = Room.objects.filter(hotel=user)
        elif type == 'agency':
            q = Tour.objects.filter(travel_agency=user)
        else:
            q = Flight.objects.filter(airline=user)

        if q != None:
            for foo in q.all():
                s = {}
                s['image'] = foo.image
                s['name'] = foo.__str__()
                s['number'] = foo.sold_number
                s['capacity'] = foo.capacity
                if type == 'hotel':
                    s['expired'] = foo.end_date < datetime.datetime.now().date()
                elif type == 'agency':
                    s['expired'] = foo.going_date < datetime.datetime.now().date()
                else:
                    s['expired'] = foo.date < datetime.datetime.now().date()
                s['price'] = foo.price
                service.append(s)
        capacityadd = CapacityAddingForm()

        return render(request, 'service_provider/type_service_list.html', {'services': service, 'capa': capacityadd})

@service_provider_required()
def add_capacity(request):
    print("salaaaaaaaam")
    print(request.POST)
    if request.method == 'POST':
        print("Hi")
        print(request.POST)
        form = CapacityAddingForm(request.POST)
        if form.is_valid():
            service = Service.objects.get(sold_number=form.cleaned_data['sold_number'])
            print(service.sold_number)
            print(service.capacity)
            service.capacity += form.cleaned_data['added_capacity']
            service.save()
    return redirect(reverse('provider_service_list'))