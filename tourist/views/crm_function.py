__author__ = 'آرمان'

from django.shortcuts import render
from sepas_iran.tourist.models import Tourist
from django.http import Http404
from django.core.mail import send_mail
from datetime import datetime, timedelta, timezone
from celery.schedules import crontab
from celery.task import periodic_task

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
# Create your views here.


def loyalty(user_id):
    try:
        tourist = Tourist.objects.get(id=user_id)
    except Tourist.DoesNotExist:
        return Http404

    comments_count = tourist.comments.count()
    prices = [bought_service.service.cost for bought_service in tourist.boughtservice_set]
    sum_buy = sum(prices)


def send_news():
    tourists = Tourist.objects.all()
    email_text = 'service haye jadid'
    for tourist in tourists:
        send_mail('تورهای جدید', email_text, 'from@example.com', [tourist.user.email], fail_silently=False)


@periodic_task(run_every=crontab(minute=0, hour=8))
def send_happy_birthday():
    now = datetime.now(timezone.utc)
    tourists = Tourist.objects.filter(birthday=datetime.date(now))

    for tourist in tourists:
        send_mail('تولدت مبارک', 'سلام. تولدت مبارک! صد سال به این سال ها.', 'from@example.com',
                  [tourist.primary_user.email], fail_silently=False)
