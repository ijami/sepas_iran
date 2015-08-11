from django.db import models
from django.contrib.auth.models import User

from base.models import SiteUser


class ServiceProvider(SiteUser):
    name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=200)
    long_description = models.TextField(null=True, blank=True)
    advertise_image = models.ImageField(upload_to='service_provider/images/advertisement')
    SERVICE_PROVIDER_TYPE = (
        ('H', '???'),
        ('T', '????? ????? ??????? (???)'),
        ('A', '?????????'),
    )
    service_provider_type = models.CharField(max_length=1, choices=SERVICE_PROVIDER_TYPE, default=None)



class Hotel(ServiceProvider):
    degree = models.IntegerField()
    has_restaurant = models.BooleanField()
    has_parking = models.BooleanField()
    has_internet = models.BooleanField()
    has_pool = models.BooleanField()
    has_conference_hall = models.BooleanField()
    map_widget = models.CharField(max_length=500)

class AirLine(ServiceProvider):
    is_international = models.BooleanField()


class TravelAgency(ServiceProvider):
    pass