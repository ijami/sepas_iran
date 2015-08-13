__author__ = 'Javad'
from django.shortcuts import render
from django.contrib.auth import authenticate, login

from tourist.views.crm_function import loyalty
from tourist.models import Tourist
from django.contrib.auth.models import User
from base.views.send_mail import send_mail
from datetime import datetime


def home(request):
    users = User.objects.all()
        #  tourists = Tourist.objects.all()
    for user in users:
        print(str(user.id)+"\n")
    # for tourist in users:
    #     send_mail('تولدت مبارک', 'samanasoftware@gmail.com', [tourist.email], 'tourist/mail_birthday.txt',
    #                   'tourist/mail_birthday.html', {'user': tourist,'date': datetime.now()}, True)
    users = User.objects.all()
    tourists = Tourist.objects.all()
    for tourist in tourists:
        print("\n comment count" + str(tourist.comments.count())+"\n")
    print("\n    kiiiiilll  Biiiiiiiilllll \n"+ str(users.count()))
    for tourist in users:
        loyalty(tourist.id)
    return render(request, 'base/home.html')
