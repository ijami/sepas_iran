from abc import abstractmethod
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
from polymorphic.polymorphic_model import PolymorphicModel
from base.models import SiteUser


class Manager(SiteUser):

    def __str__(self):
        return self.primary_user.username


class AdvertiseBox(models.Model):
    pass


class Advertise(PolymorphicModel):

    def __init__(self, **kwargs):
        super(Advertise, self).__init__(**kwargs)
        self.service_provider = None

    def get_service_provider(self):
        return self.service_provider


class HotelAdvertise(Advertise):
    service_provider = models.ForeignKey('service_provider.Hotel')

    # def get_service_provider(self):
    #     return self.service_provider


class AirLineAdvertise(Advertise):
    service_provider = models.ForeignKey('service_provider.AirLine')

    # def get_service_provider(self):
    #     return self.service_provider


class TravelAgencyAdvertise(Advertise):
    service_provider = models.ForeignKey('service_provider.TravelAgency')