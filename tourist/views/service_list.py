import datetime

__author__ = 'MJR'
from sale.models import Factor
from django.shortcuts import render
from django.conf import settings

def service_list(request):
    print("salam")
    tourist = request.user.site_user
    item_list = []
    factors = Factor.objects.filter(tourist=tourist).all()
    for f in factors:
        items = f.items.all()
        for i in items:
            item_list.append(i)
    for f in item_list:
        print(f)
    context = {'services': item_list}
    return render(request, 'tourist/services.html', context)
