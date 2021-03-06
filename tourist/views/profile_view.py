from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render
from django.conf import settings
from base.models import SiteUser
from base.views.decorators import tourist_required
import jdatetime
__author__ = 'Iman'

@tourist_required()
def profile_view(request):
    if request.method == 'GET':
        tourist = request.user.site_user.tourist
        if tourist:
            context = {
                'name': tourist.primary_user.first_name + " " + tourist.primary_user.last_name,
                'user_name': tourist.primary_user.username,
                'address': tourist.location.address,
                'mail': tourist.primary_user.email,
                'phone': tourist.telephone,
                'birth_day': jdatetime.date.fromgregorian(date=tourist.birth_day).strftime("%Y/%m/%d"),
                'image': tourist.image,
            }
            return render(request, 'tourist/profile.html', context)
        return HttpResponse("You don't have permition to this page")


def information(request, user_id):
    tourist = SiteUser.objects.get(id=user_id)
    if tourist.get_fields()['type'] == 'tourist':
        context = {
                'name': tourist.primary_user.first_name + " " + tourist.primary_user.last_name,
                'user_name': tourist.primary_user.username,
                'address': tourist.location.address,
                'mail': tourist.primary_user.email,
                'phone': tourist.telephone,
                'birth_day': jdatetime.date.fromgregorian(date=tourist.birth_day).strftime("%Y/%m/%d"),
                'image': tourist.image,
        }
        return render(request, 'tourist/information.html', context)