from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.urlresolvers import reverse
from sale.models import ServiceItem, Cart
from service.models import Service

__author__ = 'Ehsan'

@login_required
def cart_view(request):
    tourist = request.user.site_user
    if request.method == "POST":
        myId = request.POST.get("ProductId")
        service = Service.objects.get(id=myId)
        tourist.cart.items.insert(service)
        serviceItem = ServiceItem(service=service)
        serviceItem.cart = tourist.cart
        serviceItem.number = 1
#       ServiceItem.objects.filter(cart=tourist.cart, service=service)
        serviceItem.save()
    serviceItems = ServiceItem.objects.filter(cart=tourist.cart)
    sum = 0
    for serv in serviceItems:
        sum = sum + serv.number*serv.service.price
        serv.range = range(1, serv.service.capacity - len(ServiceItem.objects.filter(service=serv.service, cart=None)) + 1)
    sum2 = sum
#    sum2 = sum*loyalty(tourist.id)
    return render(request, 'sale/cart.html', {'serviceItems': serviceItems, 'sum': sum, 'sum2': sum2})
