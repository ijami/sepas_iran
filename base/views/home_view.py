__author__ = 'Javad'
from django.shortcuts import render
from django.contrib.auth import authenticate, login

from tourist.views.crm_function import loyalty
from tourist.models import Tourist
from django.contrib.auth.models import User
from base.views.send_mail import send_mail
from datetime import datetime
from django.db.models import Max
from itertools import chain
from service.models import Service
from sale.models import ServiceItem

from tourist.views.crm_function import send_recommended_mail
def home(request):

    # tourists = Tourist.objects.all()
    # for tourist in tourists:
    #     tours_past = tourist.factors.all()
    #     for factor in tours_past:
    #         boughts = Service.objects.filter(id__in=ServiceItem.objects.filter(factor=factor)
    #                                      .values_list('service__id', flat=True))
    #
    #     recs =send_recommended_mail(tourist.primary_user.id)
    #     for rec in boughts:
    #         if rec.get_type() == 'f':
    #             send_mail('happy 8 birthday', 'b.i.sepasiran@gmail.com', [tourist.primary_user.email], 'tourist/mail_birthday.txt',
    #                         'tourist/recommendation.html', {'rec': rec,'tr':rec.airline.name,'au':rec.destination.name}, True)
    #         if rec.get_type() == 't':
    #             send_mail('happy 8 birthday', 'b.i.sepasiran@gmail.com', [tourist.primary_user.email], 'tourist/mail_birthday.txt',
    #                         'tourist/recommendation.html', {'rec': rec,'tr':rec.travel_agency.name,'au':rec.destination.name}, True)
    #         if rec.get_type() == 'r':
    #             send_mail('happy 8 birthday', 'b.i.sepasiran@gmail.com', [tourist.primary_user.email], 'tourist/mail_birthday.txt',
    #                         'tourist/recommendation.html', {'rec': rec,'tr':rec.hotel.name,'au':rec.destination.name}, True)
    #     for rec in recs:
    #         if rec.get_type() == 'f':
    #             send_mail('happy 9 birthday', 'b.i.sepasiran@gmail.com', [tourist.primary_user.email], 'tourist/mail_birthday.txt',
    #                         'tourist/recommendation.html', {'rec': rec,'tr':rec.airline.name,'au':rec.destination.name}, True)
    #         if rec.get_type() == 't':
    #             send_mail('happy 9 birthday', 'b.i.sepasiran@gmail.com', [tourist.primary_user.email], 'tourist/mail_birthday.txt',
    #                         'tourist/recommendation.html', {'rec': rec,'tr':rec.travel_agency.name,'au':rec.destination.name}, True)
    #         if rec.get_type() == 'r':
    #             send_mail('happy 9 birthday', 'b.i.sepasiran@gmail.com', [tourist.primary_user.email], 'tourist/mail_birthday.txt',
    #                         'tourist/recommendation.html', {'rec': rec,'tr':rec.hotel.name,'au':rec.destination.name}, True)
    #

    return render(request, 'base/home.html')



    # users = User.objects.all()
    #     #  tourists = Tourist.objects.all()
    # for user in users:
    #     print(str(user.id)+" =user_id\n")
    # print (str(users.latest('id'))+"\n -> "+str(str(users.latest('id').id)=="3"))
    #
    # # e = list(chain(users,users ))
    # e = []
    # e.append(users.latest('id'))
    # e.append(users.earliest('id'))
    # e.append(users.latest('id'))
    # e.sort(key=lambda x: x.id)
    # # e = e.extend(User.objects.filter(id=2).all())
    # print("\n --->  "+str(str(e[1].id) == str(e[2].id))+"  "+str(e[0].id)+" "+str(e[e.__len__()-1].id)+" ** "+str(e.__len__())+" ++ \n")
    # # for tourist in users:
    #     send_mail('تولدت مبارک', 'samanasoftware@gmail.com', [tourist.email], 'tourist/mail_birthday.txt',
    #                   'tourist/mail_birthday.html', {'user': tourist,'date': datetime.now()}, True)

    # users = User.objects.all()
    # tourists = Tourist.objects.all()
    # for tourist in tourists:
    #     print("\n comment count" + str(tourist.comments.count())+"\n")
    # print("\n    kiiiiilll  Biiiiiiiilllll \n"+ str(users.count()))
    # for tourist in users:
    #     loyalty(tourist.id)
