import os

from django.contrib.auth.models import User
from django.db import models

from polymorphic.polymorphic_model import PolymorphicModel


def get_image_path(instance, filename):
    folder_name = str(instance.user.username)
    return os.path.join('images/profile_images/', folder_name, filename)


class SiteUser(PolymorphicModel):
    primary_user = models.OneToOneField(User, related_name='site_user')
    location = models.ForeignKey('Location', null=True, blank=True, related_name='location_owner')
    image = models.ImageField(upload_to='base/profile_images/', blank=True, null=True)
    telephone = models.CharField(max_length=20)

    def get_fields(self):
        pass

    def get_cart_num(self):
        return 0

    def __str__(self):
        return self.primary_user.get_short_name()

class Location(models.Model):
    city = models.ForeignKey('City', related_name='locations')
    address = models.TextField()

    def __str__(self):
        return self.city.__str__() + ": " + self.address

class City(models.Model):
    name = models.CharField(max_length=100)
    map_code = models.CharField(max_length=10)
    collection = models.ForeignKey('CityCollection', null=True, blank=True)

    def __str__(self):
        return self.name


class CityCollection(models.Model):
    name = models.CharField(max_length=100)


