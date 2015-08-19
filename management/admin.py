
# Register your models here.
from django.contrib import admin
from management.models import AdvertiseBox
from sale.models import Cart, Factor, ServiceItem


class ServiceInline(admin.TabularInline):
    model = ServiceItem


class CartAdmin(admin.ModelAdmin):
    inlines = [ServiceInline]


class FactorAdmin(admin.ModelAdmin):
    inlines = [ServiceInline]

admin.site.register(Cart, CartAdmin)
admin.site.register(Factor)
admin.site.register(AdvertiseBox)
