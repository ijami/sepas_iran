__author__ = 'آرمان'

from django.shortcuts import render
from tourist.models import Tourist
from service.models import Flight
from service.models import Airport
from django.http import Http404
from django.core.mail import send_mail
from datetime import datetime, timedelta, timezone
from celery.schedules import crontab
from celery.task import periodic_task
from service.models import Service,Tour
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from datetime import datetime, timedelta, timezone

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
def send_recommended_mail(user_id):
    try:
        tourist = Tourist.objects.get(id=user_id)
    except Tourist.DoesNotExist:
        return Http404
    tours_past = tourist.factors.all()
    tours_recommended = []
    for factor in tours_past:
        ariports = factor.serviceitem_set.all().filter(instanceof=Flight)
        for tour in ariports:
            tour.destination
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
