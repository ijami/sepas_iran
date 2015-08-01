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

    def __str__(self):
        return self.city.__str__() + ": " + self.address


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
