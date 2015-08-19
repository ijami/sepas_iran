from datetime import date
import datetime
from django.shortcuts import render
from sale.models import Factor, ServiceItem, Cart
from service.models import Service

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
    post = request.POST
    print(post)
    for key in post:
        print("naddaf " , key[0:8])
        if key[0:8] != "quantity":
            continue



        value = post[key]
        string = key[9:]
        # print("at first : " , value, " ", string)
        # if key[0:8] != "quantity_":
        #     break
        service = Service.objects.get(sold_number=string)
        c = Cart.objects.get(tourist=request.user.site_user)
        si = ServiceItem.objects.get(service=service, factor=None, cart=c)
        si.number = int(value)
        # print("iman is ", si.number)
        si.save()
    return render(request, 'sale/bank.html')
