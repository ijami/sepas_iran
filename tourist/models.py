# Create your models here.
from django.contrib.auth.models import User
from django.db import models

from base.models import SiteUser


class Tourist(SiteUser):
    birth_day = models.DateField()
    cart = models.OneToOneField('sale.Cart', related_name='tourist')

    def get_fields(self):
        return {'type': 'tourist', 'super_type': 'manager'}

    def __str__(self):
        return self.primary_user.site_user.primary_user.get_full_name() + " (" + \
            self.primary_user.username + ")"
