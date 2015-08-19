from datetime import date
import datetime
from django.shortcuts import render
from sale.models import Factor, ServiceItem

__author__ = 'MJR'
from base.views.decorators import tourist_required

@tourist_required()
def buy(request):
    user = request.user.site_user
    cart = user.cart
    factor = Factor()
    factor.create_date = datetime.datetime.now()
    factor.tourist = user
    factor.save()
    serviceItems = ServiceItem.objects.filter(cart=user.cart)
    for si in cart.items.all():
        si.cart = None
        si.factor = factor
        si.save()
    return render(request, 'sale/success.html', {'serviceItems': serviceItems})


def bank(request):
    return render(request, 'sale/bank.html')
