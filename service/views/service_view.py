__author__ = 'Mohsen'

from django.shortcuts import render
from service.models import Service, Tour, Flight, Room, City
from service.forms import SearchServiceListForm
from django.http import HttpResponse
from tourist.views.crm_function import sold_count

def show_type_service_list_view(request, type):
    max_price = 0
    max_price = Tour.objects.all().latest('price')
    max_price = Flight.objects.all().latest('price') if (Flight.objects.all().latest('price').price > max_price.price) else max_price
    max_price = Room.objects.all().latest('price') if (Room.objects.all().latest('price').price > max_price.price) else max_price
    if request.method == 'POST':
        form = SearchServiceListForm(request.POST)
        if form.is_valid():
            str = form.cleaned_data['price_range']
            rng = [int(s) for s in str.split() if s.isdigit()]
            origin = form.cleaned_data['origin']
            destination = form.cleaned_data['destination']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']



            if type == 'tour':
                service = Tour.objects.filter(price__lte=rng[0], price__gte=rng[1])
                if origin != None:
                    print('origin')
                    service = service.filter(origin__name=origin.name)
                if destination != None:
                    print('destination')
                    service = service.filter(destination__name=destination.name)
                if start_date != None:
                    print(start_date)
                    service = service.filter(going_date__gte=start_date)
                if end_date != None:
                    print(end_date)
                    service = service.filter(return_date__lte=end_date)

            elif type == 'flight':
                service = Flight.objects.filter(price__lte=rng[0], price__gte=rng[1])

                if origin != None:
                    print('origin')
                    service = service.filter(origin__name=origin.name)
                if destination != None:
                    print('destination')
                    service = service.filter(destination__name=destination.name)
                if start_date != None:
                    print(start_date)
                    service = service.filter(date__gte=start_date)
                if end_date != None:
                    print(end_date)
                    service = service.filter(date__lte=end_date)

            elif type == 'room':
                service = Room.objects.filter(price__lte=rng[0], price__gte=rng[1])

                if origin != None:
                    print('origin')
                    service = service.filter(origin=origin)
                if destination != None:
                    print('destination')
                    service = service.filter(destination__name=destination.name)
                if start_date != None:
                    print(start_date)
                    service = service.filter(start_date__gte=start_date)
                if end_date != None:
                    print(end_date)
                    service = service.filter(end_date__lte=end_date)
        else:
            return HttpResponse(form.errors)

        solds = []

        for srv in service:
            solds.append(sold_count(srv.sold_number));

        return render(request, 'type_service_list.html', {
            'service_sold': zip(service, solds),
            'type': type,
            'form': form,
            'max_price': max_price
        })
    elif request.method == 'GET':
        form = SearchServiceListForm

        if type == 'tour':
            service = Tour.objects.all()
            max_price = Tour.objects.all().latest('price')

        elif type == 'flight':
            service = Flight.objects.all()
            max_price = Flight.objects.all().latest('price')

        elif type == 'room':
            service = Room.objects.all()
            max_price = Room.objects.all().latest('price')

        solds = []

        for srv in service:
            solds.append(sold_count(srv.sold_number));

        return render(request, 'type_service_list.html', {
            'service_sold': zip(service, solds),
            'max_price': max_price,
            'type': type,
            'form': form


        })
