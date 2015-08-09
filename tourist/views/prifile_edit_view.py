from django.core.urlresolvers import reverse
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from tourist.forms import TouristEditProfileForm

__author__ = 'Iman'


def profile_edit_view(request):
    if request.method == 'GET':
        if request.user.site_user.tourist:
            tourist = request.user.site_user.tourist
            edit_profile_form = TouristEditProfileForm(instance=tourist)
            image = request.user.site_user.image
            return render(request, 'tourist/profile_modify.html', {'form': edit_profile_form, 'image': image})
    elif request.method == 'POST':
        form = TouristEditProfileForm(request.POST, request.FILES)
        form.save()
        return redirect(reverse('panel'))
