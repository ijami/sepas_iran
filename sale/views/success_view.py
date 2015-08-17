import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.urlresolvers import reverse
from sale.models import ServiceItem, Cart, Factor
from service.models import Service

__author__ = 'Ehsan'

@login_required
def success_view(request):
    tourist = request.user.site_user
    serviceItems = ServiceItem.objects.filter(cart=tourist.cart)
    factor = Factor()
    factor.tourist = tourist
    factor.create_date = str(datetime.datetime.now())
    factor.save()
    for serv in serviceItems:
        serv.factor = factor
        serv.cart = None
    factorNum = Factor.objects.all().count()
    return render(request, 'sale/success.html', {'serviceItems': serviceItems,'factorNum': factorNum})

