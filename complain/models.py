from django.db import models

from sale.models import ServiceItem
from tourist.models import Tourist


# Create your models here.

class Complain(models.Model):

    STATES = (('Q', 'در صف بررسی'), ('H', 'در حال بررسی'), ('S', 'صدور حکم'), ('F', 'پایان یافته'))

    service_item = models.ForeignKey(ServiceItem)
    text = models.TextField()
    title = models.CharField(max_length=300)
    create_date = models.DateTimeField(auto_now_add=True)
    state = models.CharField(max_length=10, choices=STATES, default='Q')
    last_state_change = models.DateTimeField(auto_now=True)


class Poll(models.Model):

    PRICE_STATE = (('G', 'مناسب'), ('E', 'گران'), ('C', 'ارزان'))

    service_item = models.ForeignKey(ServiceItem, related_name='polls')
    create_date = models.DateTimeField(auto_now_add=True)
    rate = models.IntegerField()
    price_state = models.CharField(max_length=10, choices=PRICE_STATE)


class RoomPoll(Poll):
    food_rate = models.IntegerField()
    workers_rate = models.IntegerField()
    cleanliness_rate = models.IntegerField()


class FlightPoll(Poll):
    was_on_time = models.BooleanField()
    workers_rate = models.IntegerField()
    pilot_rate = models.IntegerField()


class TourPoll(Poll):
    guide_rate = models.BooleanField()
    discipline_rate = models.IntegerField()
    hotel_rate = models.IntegerField()
    flight_rate = models.IntegerField()



