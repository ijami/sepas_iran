from django.shortcuts import render
from base.models import SiteUser

__author__ = 'MJR'


def information(request, id):
    user = SiteUser.objects.get(id=id)
    context = user.get_fields()
    data = {'context': context}
    return render(request, 'service_provider/provider_information.html', data)