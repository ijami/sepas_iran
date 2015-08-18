__author__ = 'آرمان'

from django.shortcuts import render
from tourist.models import Tourist
from service.models import Flight,Room,Tour,Comment
from service.models import Airport
from sale.views.finance import tourist_services
from django.http import Http404
from service.models import Service,Tour
from django.contrib.auth.models import User
from datetime import datetime, timedelta, timezone
from django.db.models import Max
from base.models import City
from sale.models import ServiceItem
# Create your views here.


def loyalty(user_id):
    try:
        tourist = User.objects.get(id=user_id)
    except Tourist.DoesNotExist:
        return Http404
    time_now=datetime.now().date().year * 365 +datetime.now().date().month*30 + datetime.now().date().day
    time_joined = tourist.date_joined.year * 365 +tourist.date_joined.month*30 + tourist.date_joined.day
    print("\ntime joining   " + str(time_now -time_joined)+"\n")
    
    # comments_count = tourist.comments.count()
    # comments_count= 0
    # print("\n%%%%%   "+str(time_joining)+ "  " + str(comments_count)+" %%%%%%%\n" )
    # prices = [bought_service.service.cost for bought_service in tourist.boughtservice_set]
    # sum_buy = sum(prices)

def tourist_comments_count(tourist_id):
    services = tourist_services(tourist_id)
    counter =0
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
        flights = ServiceItem.objects.filter(factor=factor).filter(type=Flight)
        flights_exist = Flight.get_exist()
        for flight in flights:
            airports = Airport.objects.filter(city=flight.destination.city)
            flight_city = []
            for airport in airports:
                flight_city.append(flights_exist.filter(destination=airport).all().latest('sold_number'))
            recommended.append(flight_city.sort(key=lambda x: x.sold_number)[flight_city.__len__()-1])

        tours = ServiceItem.objects.filter(factor=factor).filter(type=Tour)
        tours_exist = Tour.get_exist()
        for tour in tours :
            cities = City.objects.filter(collection=tour.destination.collection)
            for tour_city in cities:
                if tour_city != tour.destination:
                    recommended.append(tours_exist.filter(destination=tour_city).all().latest('sold_number'))

    return recommended


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
