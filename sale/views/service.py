import datetime
from django.core.exceptions import ObjectDoesNotExist
import jdatetime

__author__ = 'MJR'
from django.shortcuts import render, redirect
from service.models import Service
from django.http import Http404
from sale.models import Factor, ServiceItem
import sys

def service_show(request, sold_number):
    print(sold_number)
    try:
        service = Service.objects.get(sold_number=sold_number)
    except ObjectDoesNotExist:
        print('exception')
        raise Http404
    t = service.get_type()
    print("abt")
    print(service.is_exp())
    start_date = None
    end_date = None
    hour = None
    if t == 'r':
        type = 'هتل'
        provider = service.hotel
        start_date = jdatetime.date.fromgregorian(date=service.start_date).strftime("%Y/%m/%d")
        end_date = jdatetime.date.fromgregorian(date=service.end_date).strftime("%Y/%m/%d")
    elif t == 't':
        type = 'تور'
        provider = service.travel_agency
        start_date = jdatetime.date.fromgregorian(date=service.going_date).strftime("%Y/%m/%d")
        end_date = jdatetime.date.fromgregorian(date=service.return_date).strftime("%Y/%m/%d")
    elif t == 'f':
        type = 'پرواز'
        provider = service.airline
        start_date = jdatetime.date.fromgregorian(date=service.date).strftime("%Y/%m/%d")
    q = ServiceItem.objects.filter(service=service, cart=None).strftime("%Y/%m/%d")
    size = 0
    for x in q.all():
        size += x.number
        print(size)
    size = len(q)
    remain = service.capacity - size
    comments = service.comments.all()
    cm = []
    for c in comments:
        print(c.send_time.date())
        cm.append({
            'text': c.text,
            'sender': c.sender,
            'send_time': jdatetime.date.fromgregorian(date=c.send_time.date())
        })
    context = {
        'type': type,
        'image': service.image,
        'name': service.__str__(),
        'tagline': service.tag_line,
        'exist': True if (service.capacity - size) > 0 else False,
        'remain': remain,
        'price': service.price,
        'service': service,
        'comments': cm,
        'provider': provider,
        'start_date': start_date,
        'end_date': end_date
    }
    return render(request, 'sale/service.html', context)