from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Manager(models.Model):
    primary_user = models.ForeignKey(User)
