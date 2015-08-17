from django.db import models
from polymorphic.polymorphic_model import PolymorphicModel
from datetime import datetime, timedelta, timezone
from base.models import City, SiteUser
from service_provider.models import AirLine, Hotel, TravelAgency
from tourist.models import Tourist


class Service(PolymorphicModel):
    price = models.IntegerField()
    capacity = models.IntegerField()
    sold_number = models.CharField(max_length=20)
    tag_line = models.CharField(max_length=255)

    @staticmethod
    def get_exist(self):
        pass
    image = models.ImageField(upload_to='base/service_images/', blank=True, null=True)



class Comment(models.Model):
    sender = models.ForeignKey(SiteUser, related_name='comments')
    text = models.TextField()
    send_time = models.DateTimeField(auto_now=True)
    service = models.ForeignKey('Service', related_name='comments')

    def __str__(self):
        return self.sender.primary_user.username + ": " + self.text


class Flight(Service):
    flight_number = models.CharField(max_length=20)
    airline = models.ForeignKey(AirLine, related_name='flights')
    origin = models.ForeignKey('Airport', related_name='departures')
    destination = models.ForeignKey('Airport', related_name='arrivals')
    time = models.DateTimeField()
    @staticmethod
    def get_exist(self):
        return Flight.objects.filter(time__lt=(datetime.now()))
    origin = models.ForeignKey('base.City', related_name='flight_departures')
    destination = models.ForeignKey('base.City', related_name='flight_arrivals')
    date = models.DateTimeField()
    time = models.TimeField()
    airplane = models.CharField(max_length=40)

    def __str__(self):
        return self.flight_number + ": " + "از" + self.origin.name + "به"\
               + self.destination.name


class Room(Service):
    start_date = models.DateField()
    end_date = models.DateField()
    hotel = models.ForeignKey(Hotel, related_name='rooms')
    number_of_bed = models.IntegerField()
    has_television = models.BooleanField(default=False)
    has_telephone = models.BooleanField(default=False)
    has_bathroom = models.BooleanField(default=False)
    def get_city(self):
        return self.hotel.location.city
    @staticmethod
    def get_exist(self):
        return Room.objects.filter(time__lt=(datetime.now()))

    def __str__(self):
        return self.hotel.name + ": " + "اتاق " + str(self.number_of_bed) + "تخته"


class Tour(Service):
    travel_agency = models.ForeignKey(TravelAgency, related_name='tours')
    origin = models.ForeignKey('base.City', related_name='departures')
    destination = models.ForeignKey('base.City', related_name='arrivals')
    # airline = models.ForeignKey(AirLine)
    going_date = models.DateField()
    return_date = models.DateField()
    description = models.TextField()
    # going_flight = models.ForeignKey('Flight', null=True, blank=True, related_name='going_tours')
    # return_flight = models.ForeignKey('Flight', null=True, blank=True, related_name='return_tours')
    # hotel = models.ForeignKey('service_provider.Hotel', null=True, blank=True)
    hotel_name = models.CharField(max_length=100, null=True, blank=True)

    tour_guide_name = models.CharField(max_length=100)
    @staticmethod
    def get_exist(self):
        return Tour.objects.filter(time__lt=(datetime.now()))

    # tour_guide_name = models.CharField(max_length=100)


    def __str__(self):
        return self.travel_agency.name + ": " + "از " + self.origin.name + " به " + self.destination.name


class Airport(models.Model):
    name = models.CharField(max_length=60)
    city = models.ForeignKey(City, related_name='airports')
    address = models.TextField()

    def __str__(self):
        return self.city.name + ": " + self.name
