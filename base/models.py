from django.contrib.auth.models import User
from django.db import models
import os

# Create your models here.
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
        return self.cart.items.count()


class Location(models.Model):
    city = models.ForeignKey('City', related_name='locations')
    address = models.TextField()

class City(models.Model):
    name = models.CharField(max_length=100)
    collection = models.ForeignKey('CityCollection', null=True, blank=True)

    def __str__(self):
        return self.name


class CityCollection(models.Model):
    name = models.CharField(max_length=100)

