from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render

from sale.views.finance import tourist_flights,\
    tourist_rooms, tourist_services,\
    tourist_services_price, tourist_services_waited, tourist_tours,tourist_services_used
from tourist.views.crm_function import tourist_comments_count


@login_required
def reprot_view(request):
    if request.method == 'GET':
        tourist = request.user.site_user.tourist
        if tourist:
            context = {
                'service_bought': tourist_services(tourist.id).__len__(),
                'servic_used': tourist_services_used(tourist.id).__len__(),
                'servic_waited': tourist_services_waited(tourist.id).__len__(),
                'hotel_bought': tourist_rooms(tourist.id).__len__(),
                'flight_bought': tourist_flights(tourist.id).__len__(),
                'tour_bought': tourist_tours(tourist.id).__len__(),
                'all_price' : tourist_services_price(tourist.id),
                'comment_count' : tourist_comments_count(tourist.id),
            }
            return render(request, 'tourist/report.html', context)
        return HttpResponse("You don't have permition to this page")


