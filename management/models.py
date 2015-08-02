from django.db import models
from django.contrib.auth.models import User


# Create your models here.
from base.models import SiteUser


class Manager(SiteUser):

    def __str__(self):
        return self.primary_user.username