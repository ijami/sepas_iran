from django.db import models

from base.models import City, SiteUser
from service_provider.models import AirLine, Hotel, TravelAgency
from tourist.models import Tourist


class Service(models.Model):
    price = models.IntegerField()
    capacity = models.IntegerField()
    sold_number = models.IntegerField()


class Comment(models.Model):
    sender = models.ForeignKey(SiteUser, related_name='comments')
    text = models.TextField()
    send_time = models.DateTimeField(auto_now=True)
    service = models.ForeignKey('Service', related_name='comments')

    def __str__(self):
        return self.sender.primary_user.username + ": " + self.text


class Flight(Service):
    flight_number = models.CharField(max_length=10)
    airline = models.ForeignKey(AirLine, related_name='flights')
    origin = models.ForeignKey('Airport', related_name='departures')
    destination = models.ForeignKey('Airport', related_name='arrivals')
    time = models.DateTimeField()

    def __str__(self):
        return self.flight_number + ": " + "از" + self.origin.city.name + "به"+ self.destination.city.name


class Room(Service):
    hotel = models.ForeignKey(Hotel, related_name='rooms')
    number_of_bed = models.IntegerField()
    additional_capacity = models.IntegerField()
    has_television = models.BooleanField(default=False)
    has_telephone = models.BooleanField(default=False)
    has_bathroom = models.BooleanField(default=False)

    def __str__(self):
        return self.hotel.name + ": " + "اتاق " + self.number_of_bed + "تخته"


class Tour(Service):
    travel_agency = models.ForeignKey(TravelAgency, related_name='tours')
    origin = models.ForeignKey('TourLocation', related_name='departures')
    destination = models.ForeignKey('TourLocation', related_name='arrivals')
    airline = models.ForeignKey(AirLine)
    going_date = models.DateField()
    return_date = models.DateField()
    description = models.TextField()
    going_flight = models.ForeignKey('Flight', null=True, blank=True, related_name='going_tours')
    return_flight = models.ForeignKey('Flight', null=True, blank=True, related_name='return_tours')
    hotel = models.ForeignKey('service_provider.Hotel', null=True, blank=True)
    hotel_name = models.CharField(max_length=100, null=True, blank=True)
    tour_guide_name = models.CharField(max_length=100)

    def __str__(self):
        self.travel_agency.name + ": " + "از " + self.origin.city.name + " به " + self.destination.city.name


class Airport(models.Model):
    name = models.CharField(max_length=60)
    city = models.ForeignKey(City, related_name='airports')
    address = models.TextField()

    def __str__(self):
        return self.city.name + ": " + self.name


class TourLocation(models.Model):
    city = models.ForeignKey(City, related_name='tour_locations')

