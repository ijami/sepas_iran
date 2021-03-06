from datetime import datetime

from django.db import models
import jdatetime
from polymorphic.polymorphic_model import PolymorphicModel

from base.models import City, SiteUser
from service_provider.models import AirLine, Hotel, TravelAgency
from tourist.models import Tourist
# from sale.models import ServiceItem, Factor
# from tourist.views.crm_function import sold_count
class Service(PolymorphicModel):
    price = models.IntegerField()
    capacity = models.IntegerField()
    sold_number = models.CharField(max_length=20)
    tag_line = models.CharField(max_length=255)
    image = models.ImageField(upload_to='base/service_images/', blank=True, null=True)

    @staticmethod
    def get_exist():
        pass

    def get_service_provider(self):
        pass

    def get_type(self):
        pass

    def is_exp(self):
        return self.get_date() <= datetime.now().date()

    def is_exp_2(self):
        pass

    def __str__(self):
        return self.tag_line

    def get_date(self):
        pass


class Comment(models.Model):
    sender = models.ForeignKey(SiteUser, related_name='comments')
    text = models.TextField()
    send_time = models.DateTimeField(auto_now=True)
    service = models.ForeignKey('Service', related_name='comments')

    def __str__(self):
        return self.sender.primary_user.username + ": " + self.text

    def get_city(self):
        pass


class Flight(Service):
    flight_number = models.CharField(max_length=20)
    airline = models.ForeignKey(AirLine, related_name='flights')
    type = models.CharField(max_length=10, default="Flight")
    origin = models.ForeignKey('base.City', related_name='flight_departures')
    destination = models.ForeignKey('base.City', related_name='flight_arrivals')
    date = models.DateField()
    time = models.TimeField()
    airplane = models.CharField(max_length=40)


    @staticmethod
    def get_exist():
        return Flight.objects.filter(date__gt=(datetime.now()))


    def __str__(self):

        return self.airline.name + " : " +  " \n " + " از " + self.origin.name + " به "  + self.destination.name

    def get_service_provider(self):
        return self.airline

    def get_type(self):
        return 'f'


    def get_persian_date(self):
        return jdatetime.date.fromgregorian(date=self.date).strftime("%Y/%m/%d")

    def get_date(self):
        return self.date

    def get_city(self):
        return self.destination

    def is_exp_2(self):
        return self.is_exp()

class Room(Service):
    start_date = models.DateField()
    end_date = models.DateField()
    hotel = models.ForeignKey(Hotel, related_name='rooms')
    number_of_bed = models.IntegerField()
    has_television = models.BooleanField(default=False)
    has_telephone = models.BooleanField(default=False)
    has_bathroom = models.BooleanField(default=False)
    type = models.CharField(max_length=10, default="Room")

    def get_service_provider(self):
        return self.hotel

    def get_city(self):
        return self.hotel.location.city

    @staticmethod
    def get_exist():
        return Room.objects.filter(end_date__gt=(datetime.now()))

    def __str__(self):
        return self.hotel.name + ": " + "اتاق " + str(self.number_of_bed) + " تخته "

    def get_type(self):
        return 'r'

    def is_exp_2(self):
        return self.end_date <= datetime.now().date()

    def get_persian_start_date(self):
        return jdatetime.date.fromgregorian(date=self.start_date).strftime("%Y/%m/%d")
    def get_persian_end_date(self):
        return jdatetime.date.fromgregorian(date=self.end_date).strftime("%Y/%m/%d")

    def get_date(self):
        return self.start_date


    def get_city(self):
        return self.hotel.location.city


class Tour(Service):
    travel_agency = models.ForeignKey(TravelAgency, related_name='tours')
    origin = models.ForeignKey('base.City', related_name='departures')
    destination = models.ForeignKey('base.City', related_name='arrivals')
    # airline = models.ForeignKey(AirLine)
    going_date = models.DateField()
    return_date = models.DateField()
    description = models.TextField()
    trans_type = models.CharField(max_length=6, default='plane')
    # going_flight = models.ForeignKey('Flight', null=True, blank=True, related_name='going_tours')
    # return_flight = models.ForeignKey('Flight', null=True, blank=True, related_name='return_tours')
    # hotel = models.ForeignKey('service_provider.Hotel', null=True, blank=True)
    hotel_name = models.CharField(max_length=100, null=True, blank=True)

    tour_guide_name = models.CharField(max_length=100)

    type = models.CharField(max_length=10, default="Tour")

    def get_service_provider(self):
        return self.travel_agency

    @staticmethod
    def get_exist():
        return Tour.objects.filter(return_date__gt=datetime.now())

    # tour_guide_name = models.CharField(max_length=100)

    def __str__(self):
        return self.travel_agency.name + ": \n" + " از " + self.origin.name + " به " + self.destination.name

    def get_type(self):
        return 't'


    def get_persian_going_date(self):
        return jdatetime.date.fromgregorian(date=self.going_date).strftime("%Y/%m/%d")
    def get_persian_return_date(self):
        return jdatetime.date.fromgregorian(date=self.return_date).strftime("%Y/%m/%d")

    def get_date(self):
        return self.going_date

    def get_city(self):
        return self.destination

    def is_exp_2(self):
        return self.return_date <= datetime.now().date()

class Airport(models.Model):
    name = models.CharField(max_length=60)
    city = models.ForeignKey(City, related_name='airports')
    address = models.TextField()

    def __str__(self):
        return self.city.name + ": " + self.name
