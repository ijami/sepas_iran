from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from service.models import ServiceInfo
# Create your models here.

class Tourist(models.Model):
    primary_user = models.ForeignKey(User)
    location = models.ForeignKey('Location', null=True)

class Location(models.Model):
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    province = models.CharField(max_length=30)
    address = models.TextField()

class BoughtService(models.Model):
    service = models.ForeignKey(ServiceInfo)
    tourist = models.ForeignKey(Tourist)
    date = models.DateTimeField()

class Comment(models.Model):
    tourist = models.ForeignKey(Tourist)
    text = models.TextField()
    date = models.DateTimeField()
