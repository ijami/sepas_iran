# Create your models here.
from django.db import models
from service_provider.models import ServiceProvider
# Create your models here.


class ServiceInfo(models.Model):
    service_provider = models.ForeignKey(ServiceProvider)  # foreign key be modele service provider
    type = models.CharField(max_length=30)
    cost = models.IntegerField()
    timing = models.DateTimeField()
