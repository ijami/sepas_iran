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
    cart = tourist.cart
    factor = Factor()
    factor.tourist = tourist
    factor.create_date = str(datetime.datetime.now())
    factor.save()
    d = 0
    for si in cart.items.all():
        si.cart = None
        si.factor = factor
        si.size = d;
        d += 1;
        si.save()
    factorNum = len(Factor.objects.filter(tourist=tourist))
    serviceItems = ServiceItem.objects.filter(factor=factor)
    return render(request, 'sale/success.html', {'serviceItems': serviceItems,'factorNum': factorNum})
