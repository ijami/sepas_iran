from django.shortcuts import render
from tourist.forms import TouristEditProfileForm

__author__ = 'Iman'


def profile_edit_view(request):

    if request.method == 'GET':
        if request.user.site_user.tourist:
            tourist = request.user.site_user.tourist
            edit_profile_form = TouristEditProfileForm(instance=tourist)
            return render(request, 'tourist/profile_modify.html', {'form': edit_profile_form})

