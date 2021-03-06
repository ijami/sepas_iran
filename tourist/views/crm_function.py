__author__ = 'آرمان'

from datetime import datetime

from django.http import Http404

from django.contrib.auth.models import User

from tourist.models import Tourist
from service.models import Flight, Comment
from sale.views.finance import tourist_services
from service.models import Service, Tour, Room
from base.models import City
from sale.models import ServiceItem, Factor
from sale.views.finance import tourist_services_price
from service_provider.models import ServiceProvider
# Create your views here.

def sold_count(service_sold_number):
    service = Service.objects.filter(sold_number=service_sold_number)
    factors = Factor.objects.all()
    counter = 0
    for factor in factors:
        counter += ServiceItem.objects.filter(factor=factor).filter(service=service).__len__()
    return counter


def loyalty(tourist_id):
    try:
        tourist = Tourist.objects.get(id=tourist_id)
    except Tourist.DoesNotExist:
        return Http404
    time_now = datetime.now().date().year * 365 + datetime.now().date().month * 30 + datetime.now().date().day
    time_joined = tourist.date_joined.year * 365 + tourist.date_joined.month * 30 + tourist.date_joined.day
    # print("\ntime joining   " + str(time_now - time_joined) + "\n")
    return time_now - time_joined + tourist_comments_count(tourist_id) * 100 + tourist_services_price(tourist_id)


def tourist_comments_count(tourist_id):
    services = tourist_services(tourist_id)
    counter = 0
    for service in services:
        counter += Comment.objects.filter(service=service).all().count()
    return counter


def send_recommended_mail(user_id):
    try:
        tourist = Tourist.objects.get(primary_user__id=user_id)
    except Tourist.DoesNotExist:
        return Http404
    tours_past = tourist.factors.all()
    recommended = []
    for factor in tours_past:
        flights = Service.objects.filter(id__in=ServiceItem.objects.filter(factor=factor)
                                         .values_list('service__id', flat=True)) \
            .filter(id__in=Flight.objects.all().values_list('id', flat=True))
        try:
            flights_exist = Flight.get_exist()
            # print(" ^^^^  " + str(flights_exist.__len__()) + "\n")
        except Tourist.DoesNotExist:
            return Http404

        if flights_exist:
            for flight in flights:
                # airports = Airport.objects.filter(city=flight.destination)
                cities = City.objects.filter(map_code=flight.destination.map_code)
                for tour_city in cities:
                    if flights_exist.filter(destination=tour_city):
                        flight_its = flights_exist.filter(destination=tour_city)
                        flight_max = None
                        for flight_it in flight_its:
                            if (flight_max):
                                if (sold_count(flight_it.sold_number) >= sold_count(flight_max.sold_number)):
                                    flight_max = flight_it
                            else:
                                flight_max = flight_it
                        recommended.append(flight_max)

                        # recommended.append(flights_exist.filter(destination=tour_city).latest('sold_number'))
                        # flight_city = []
                        # for airport in airports:
                        #     flight_city.append(flights_exist.filter(destination=airport).all().latest('sold_number'))
                        # # recommended.append(flight_city.sort(key=lambda x: x.sold_number)[flight_city.__len__() - 1])

        tours = Service.objects.filter(id__in=ServiceItem.objects.filter(factor=factor)
                                       .values_list('service__id', flat=True)) \
            .filter(id__in=Tour.objects.all().values_list('id', flat=True))
        try:
            tours_exist = Tour.get_exist()
        except Tourist.DoesNotExist:
            return Http404

        if tours_exist:
            for tour in tours:
                cities = City.objects.filter(map_code=tour.destination.map_code)
                for tour_city in cities:
                    if tours_exist.filter(destination=tour_city):
                        tour_its = tours_exist.filter(destination=tour_city)
                        tour_max = None
                        for tour_it in tour_its:
                            if (tour_max):
                                if (sold_count(tour_it.sold_number) >= sold_count(tour_max.sold_number)):
                                    tour_max = tour_it
                            else:
                                tour_max = tour_it
                        recommended.append(tour_max)
                        # recommended.append(tours_exist.filter(destination=tour_city).latest('sold_number'))

    return recommended


def feedback_count(service_provider):
    # service_provider = ServiceProvider.objects.filter(id=service_provider_id)
    feedback = 0

    flights = Flight.objects.filter(airline__primary_user__id=service_provider.primary_user.id)
    for flight in flights:
        feedback += Comment.objects.filter(service=flight).__len__()

    rooms = Room.objects.filter(hotel__primary_user__id=service_provider.primary_user.id)
    for room in rooms:
        feedback += Comment.objects.filter(service=room).__len__()

    tours = Tour.objects.filter(travel_agency__primary_user__id=service_provider.primary_user.id)
    for tour in tours:
        feedback += Comment.objects.filter(service=tour).__len__()
    return feedback

#
# def send_news():
#     tourists = Tourist.objects.all()
#     email_text = 'service haye jadid'
#     for tourist in tourists:
#         send_mail('تورهای جدید', email_text, 'from@example.com', [tourist.user.email], fail_silently=False)
#
#
# @periodic_task(run_every=crontab(minute=0, hour=8))
# def send_happy_birthday():
#     now = datetime.now(timezone.utc)
#     tourists = Tourist.objects.filter(birthday=datetime.date(now))
#
#     for tourist in tourists:
#         send_mail('تولدت مبارک', 'سلام. تولدت مبارک! صد سال به این سال ها.', 'from@example.com',
#                   [tourist.primary_user.email], fail_silently=False)
