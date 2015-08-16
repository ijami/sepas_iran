from django.db import models
from django.contrib.auth.models import User

from base.models import SiteUser
class ServiceProvider(SiteUser):
    name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=200)
    long_description = models.TextField(null=True, blank=True)
    advertise_image = models.ImageField(upload_to='service_provider/images/advertisement')




class Hotel(ServiceProvider):
    degree = models.IntegerField()
    has_restaurant = models.BooleanField(default=False)
    has_parking = models.BooleanField(default=False)
    has_internet = models.BooleanField(default=False)
    has_pool = models.BooleanField(default=False)
    has_conference_hall = models.BooleanField(default=False)
    has_fire_extinguisher = models.BooleanField(default=False)
    has_sport_salloon = models.BooleanField(default=False)
    has_health_center = models.BooleanField(default=False)
    has_coffeeshop = models.BooleanField(default=False)
    has_emergency = models.BooleanField(default=False)
    has_jungle = models.BooleanField(default=False)
    has_protection_system = models.BooleanField(default=False)
    has_shop_center = models.BooleanField(default=False)
    has_gamenet = models.BooleanField(default=False)
    has_photo_studio = models.BooleanField(default=False)

    map_widget = models.CharField(max_length=500)
    def get_fields(self):
        context = {
            'type': 'hotel',
            'image': self.image,
            'name': self.name,
            'phone': self.telephone,
            'address': self.location,
            'short_description': self.short_description,
            'long_description': self.long_description,
            'degree': self.degree,
            'has_restaurant': self.has_restaurant,
            'has_parking': self.has_parking,
            'has_internet': self.has_internet,
            'has_pool': self.has_pool,
            'has_conference_hall': self.has_conference_hall,
            'has_fire_extinguisher': self.has_fire_extinguisher,
            'has_sport_salloon': self.has_sport_salloon,
            'has_health_center': self.has_health_center,
            'has_coffeeshop': self.has_coffeeshop,
            'has_emergency': self.has_emergency,
            'has_jungle': self.has_jungle,
            'has_protection_system': self.has_protection_system,
            'has_shop_center': self.has_shop_center,
            'has_gamenet': self.has_gamenet,
            'has_photo_studio': self.has_photo_studio,
        }
        return context


class AirLine(ServiceProvider):
    is_international = models.BooleanField()

    def get_fields(self):
        context = {
            'type': 'airline',
            'image': self.image,
            'name': self.name,
            'address': self.location,
            'phone': self.telephone,
            'short_description': self.short_description,
            'long_description': self.long_description,
            'is_international': self.is_international
        }
        return context


class TravelAgency(ServiceProvider):

    def get_fields(self):
        context = {
            'type': 'agency',
            'image': self.image,
            'name': self.name,
            'address': self.location,
            'phone': self.telephone,
            'short_description': self.short_description,
            'long_description': self.long_description
        }
        return context