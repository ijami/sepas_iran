from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class SiteUser(models.Model):
    primary_user = models.OneToOneField(User, related_name='site_user')
    location = models.ForeignKey('Location', null=True, related_name='location_owner')
    image = models.ImageField(upload_to='base/images/profile_images')
    telephone = models.CharField(max_length=20)


class Location(models.Model):
    city = models.ForeignKey('City', related_name='locations')
    address = models.TextField()


class Country(models.Model):
    name = models.CharField(max_length=100)


class City(models.Model):
    country = models.ForeignKey('Country', related_name='cities')
    name = models.CharField(max_length=100)
