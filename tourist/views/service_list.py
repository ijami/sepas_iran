__author__ = 'MJR'
from sale.models import Factor
from django.shortcuts import render
from django.conf import settings

def service_list(request):
    tourist = request.user.site_user.tourist
    item_list = []
    factors = Factor.objects.filter(tourist=tourist)
    for f in factors:
        items = f.items
        for i in items:
            item_list.append(i)
    context = {'services': item_list}
    print(context['site_url'])
    return render(request, 'tourist/services.html', context)
