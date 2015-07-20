from django.db import models
from tourist.models import Tourist
from service.models import BoughtService
# Create your models here.

class Complain(models.Model):
    tourist = models.ForeignKey(Tourist)
    bought_service = models.ForeignKey(BoughtService)
    text = models.TextField()
    date = models.DateTimeField()
