from django.shortcuts import render
import jdatetime
from sale.models import Factor, ServiceItem
from service.models import Service

__author__ = 'MJR'


def information(request, id):
    service = Service.objects.get(sold_number=id)
    items = ServiceItem.objects.filter(service=service, cart=None)
    list = []
    for item in items:
        if item.factor != None:
            context = {
                'tourist': item.factor.tourist,
                'number': item.number,
                'date': jdatetime.datetime.fromgregorian(date=item.factor.create_date.date()).strftime("%Y/%m/%d"),
                'factor_num': item.service.sold_number + "_" + items.count().__str__() + "_" + Factor.objects.filter(tourist=item.factor.tourist).count().__str__()
            }
            list.append(context)
    data = {'context': list}
    return render(request, 'information.html', data)