from django.http.response import HttpResponse
from django.shortcuts import render

from sale.views.finance import tourist_flights_count,\
    tourist_rooms_count, tourist_services_count,\
    tourist_services_price, tourist_services_waited_count, tourist_tours_count,tourist_services_used_count
from tourist.views.crm_function import tourist_comments_count
from base.views.decorators import tourist_required

@tourist_required()
def reprot_view(request):
    if request.method == 'GET':
        tourist = request.user.site_user.tourist
        if tourist:
            context = {
                'service_bought': tourist_services_count(tourist.id),
                'servic_used': tourist_services_used_count(tourist.id),
                'servic_waited': tourist_services_waited_count(tourist.id),
                'hotel_bought': tourist_rooms_count(tourist.id),
                'flight_bought': tourist_flights_count(tourist.id),
                'tour_bought': tourist_tours_count(tourist.id),
                'all_price' : tourist_services_price(tourist.id),
                'comment_count' : tourist_comments_count(tourist.id),
            }
            return render(request, 'tourist/report.html', context)
        return HttpResponse("You don't have permition to this page")


