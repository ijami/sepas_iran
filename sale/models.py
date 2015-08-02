from django.db import models

from service.models import Service
from tourist.models import Tourist


class Cart(models.Model):
    last_modified = models.DateTimeField(auto_now=True)


class Factor(models.Model):
    tourist = models.ForeignKey(Tourist, related_name='factors')
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tourist.__str__() + " " + self.create_date


class ServiceItem(models.Model):
    service = models.ForeignKey(Service)
    number = models.IntegerField()
    cart = models.ForeignKey('Cart', null=True, blank=True)
    factor = models.ForeignKey('Factor', null=True, blank=True)

    def get_price(self):
        return self.number * self.service.price

    def __str__(self):
        self.service.__str__() + ": " + self.number
