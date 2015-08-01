from django.shortcuts import render

__author__ = 'Iman'

def profile_view(request):
    if request.method == 'GET':
        tourist = request.user.site_user.tourist
        if tourist:
            context = {
                'username':
            }
            return render(request, 'tourist/profile.html')

