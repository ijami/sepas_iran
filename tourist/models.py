from django.db import models


# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from base.models import SiteUser
from sale.models import Cart


class Tourist(SiteUser):
    birth_day = models.DateField()
    cart = models.OneToOneField(Cart, related_name='tourist')



