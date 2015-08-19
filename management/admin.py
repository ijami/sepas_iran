
# Register your models here.
from django.contrib import admin
from management.models import AdvertiseBox, Manager
from sale.models import Cart, Factor, ServiceItem


admin.site.register(AdvertiseBox)
admin.site.register(Manager)