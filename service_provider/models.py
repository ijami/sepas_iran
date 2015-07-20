from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class ServiceProvider(models.Model):
    primary_user = models.ForeignKey(User)
    service_type = models.CharField(max_length=50)
    details = models.TextField()
