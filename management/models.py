from django.db import models


# Create your models here.
from django.shortcuts import get_object_or_404
from base.models import SiteUser
from service_provider.models import ServiceProvider

class ManagerManager(models.Manager):
    @staticmethod
    def create():
        Manager(advertise_box=AdvertiseBox.load()).save()

class Manager(SiteUser):
    def get_fields(self):
        return {'type': 'manager', 'super_type': 'manager'}

    def __str__(self):
        return self.primary_user.username

class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.__class__.objects.exclude(id=self.id).delete()
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        try:
            return cls.objects.get()
        except cls.DoesNotExist:
            return cls()


class AdvertiseBox(SingletonModel):
    add0 = models.ForeignKey('service_provider.ServiceProvider', null=True, blank=True, related_name='add_box_0',
                             default=None)
    add1 = models.ForeignKey('service_provider.ServiceProvider', null=True, blank=True, related_name='add_box_1',
                             default=None)
    add2 = models.ForeignKey('service_provider.ServiceProvider', null=True, blank=True, related_name='add_box_2',
                             default=None)
    add3 = models.ForeignKey('service_provider.ServiceProvider', null=True, blank=True, related_name='add_box_3',
                             default=None)
    add4 = models.ForeignKey('service_provider.ServiceProvider', null=True, blank=True, related_name='add_box_4',
                             default=None)

    def set_add(self, index, service_name):
        if service_name:
            setattr(self, index, get_object_or_404(ServiceProvider, name=service_name))
        else:
            setattr(self, index, None)
        self.save()



