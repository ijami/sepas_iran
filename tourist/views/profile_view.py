from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render
from django.conf import settings
__author__ = 'Iman'

@login_required
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
                'birth_day': tourist.birth_day,
                'image': tourist.image,
            }
            return render(request, 'tourist/profile.html', context)
        return HttpResponse("You don't have permition to this page")

