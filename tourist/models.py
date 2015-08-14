# Create your models here.
from django.contrib.auth.models import User
from django.db import models

from base.models import SiteUser


class Tourist(SiteUser):
    birth_day = models.DateField()
    cart = models.OneToOneField('sale.Cart', related_name='tourist', blank=True, null=True)

    def get_fields(self):
        return {'type': 'tourist'}

    def __str__(self):
        return self.primary_user.first_name + " " + self.primary_user.last_name

    firsname = property()


