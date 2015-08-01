from django.db import models
from django.contrib.auth.models import User


# Create your models here.
from base.models import SiteUser


class Manager(models.Model):
    primary_user = models.ForeignKey(SiteUser)
