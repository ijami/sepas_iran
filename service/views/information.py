from django.shortcuts import render
import jdatetime
from sale.models import Factor, ServiceItem
from service.models import Service

__author__ = 'MJR'


def information(request, id):
    service = Service.objects.filter(sold_number=id)
    items = ServiceItem.objects.filter(service=service)
    list = []
    for item in items:
        if item.factor != None:
            context = {
                'tourist': item.factor.tourist,
                'number': item.number,
                'date': jdatetime.datetime.fromgregorian(date=item.factor.create_date.date()).strftime("%Y/%m/%d")
            }
            list.append(context)
    data = {'context': list}
    return render(request, 'information.html', data)