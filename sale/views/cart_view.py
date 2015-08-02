from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.urlresolvers import reverse
__author__ = 'Ehsan'

@login_required
def cart_view(request):
    return render(request, 'sale/cart.html')
