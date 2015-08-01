# Create your models here.
from django.contrib.auth.models import User
from django.db import models

from base.models import SiteUser


class Tourist(SiteUser):
    birth_day = models.DateField()
    cart = models.OneToOneField('sale.Cart', related_name='tourist')