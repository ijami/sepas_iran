__author__ = 'Mohsen'
from django.shortcuts import render
from service.models import Service, Tour
from tourist.views.crm_function import sold_count
from tourist.views.crm_function import send_recommended_mail

def home(request):
    new_services = Service.objects.all()[0:5]

    new_solds = []
    for srv in new_services:
        new_solds.append(sold_count(srv.sold_number))


    if request.user.is_authenticated() and request.user.site_user.get_fields()['super_type'] == 'tourist' :
        recomended_services = send_recommended_mail(request.user.id)

        recomended_solds = []
        for srv in recomended_services:
            recomended_solds.append(sold_count(srv.sold_number))

        return render(request, 'base/home.html',{
        'new_services': zip(new_services, new_solds),
        'recomended_services': zip(recomended_services, recomended_solds)
    })


    return render(request, 'base/home.html',{
        'new_services': zip(new_services, new_solds),
    })
