from datetime import date
import datetime
from django.shortcuts import render
from sale.models import Factor

__author__ = 'MJR'


def buy(request):
    user = request.user.site_user
    cart = user.cart
    factor = Factor()
    factor.create_date = datetime.datetime.now()
    factor.tourist = user
    factor.save()
    for si in cart.items.all():
        si.cart = None
        si.factor = factor
        si.save()
    return render(request, 'sale/buy.html')