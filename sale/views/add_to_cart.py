__author__ = 'MJR'

from django.shortcuts import render, redirect
from service.models import Service
from django.http import Http404
from sale.models import Factor, ServiceItem
from sale.models import Cart
from base.views.decorators import tourist_required

@tourist_required()
def add_to_cart(request):
    # print("in addtocart")
    if request.method == "POST":
        # print("sag")
        user = request.user.site_user
        if user.get_fields()['type'] == 'tourist':
            # print("khar")
            cart = user.cart
            item = ServiceItem()
            service = Service.objects.get(sold_number=request.POST['sn'])
            b = False
            for i in cart.items.all():
                if i.service == service:
                    b = True
            if b:
                return redirect('/sale/cart')
            item.service = service
            factors = Factor.objects.filter(tourist=user).all()
            # s = 0
            # for f in factors:
            #     s += len(f.items)
            # d = len(ServiceItem.objects.filter(cart=cart).all())
            item.number = 1
            item.cart = cart
            item.factor = None
            item.save()
            return redirect('/sale/cart')

@tourist_required()
def delete(request, code):
    user = request.user.site_user
    cart = user.cart
    service = Service.objects.get(sold_number=code)
    si = ServiceItem.objects.filter(service=service, cart=cart)
    si.delete()
    return redirect('/sale/cart')