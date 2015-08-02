from tourist.forms import TouristEditProfileForm

__author__ = 'Iman'


def profile_view(request):

    if request.method == 'GET':
        if request.user.site_user.tourist:
            tourist = request.user.site_user.tourist
            edit_profile_form = TouristEditProfileForm(tourist)

