__author__ = 'Mohsen'

from django.shortcuts import render
from service.models import Service, Tour, Flight, Room


def show_type_service_list_view(request, type):
    max_price = 0
    if type == 'tour':
        service = Tour.objects.all()
        if service :
            max_price = Tour.objects.all().latest('price')

    elif type == 'flight':
        service = Flight.objects.all()
        if service :
            max_price = Flight.objects.all().latest('price')

    elif type == 'hotel':
        service = Room.objects.all()
        if service :
            max_price = Room.objects.all().latest('price')




    return render(request, 'type_service_list.html', {
        'services': service,
        'max_price': max_price,
        'type': type
    })


def show_service_list_view(request):

    service = []
    service.append(Tour.objects.all())
    if service :
        max_price = Tour.objects.all().latest('price')


    flight = Flight.objects.all()


    if flight :
        service.append(flight)
        if max_price:
            max_price = Flight.objects.all().latest('price') if (Flight.objects.all().latest('price').price > max_price.price) else max_price
        else :
            max_price = Flight.objects.all().latest('price')


    room = Room.objects.all()


    if room :
        service.append(room)
        if max_price:
            max_price = Room.objects.all().latest('price') if (Room.objects.all().latest('price').price > max_price.price) else max_price
        else :
            max_price = Room.objects.all().latest('price')


    return render(request, 'service_list.html', {
        'services': service,
        'max_price': max_price,
        'Tour': Tour,
        'Flight': Flight,
        'Room': Room

    })



