from django.contrib import admin

# Register your models here.
from sale.models import Cart, Factor, ServiceItem

class ServiceInline(admin.TabularInline):
    model = ServiceItem


class CartAdmin(admin.ModelAdmin):
    inlines = [ServiceInline]



class FactorAdmin(admin.ModelAdmin):
    inlines = [ServiceInline]

admin.site.register(Cart, CartAdmin)
admin.site.register(Factor, FactorAdmin)
admin.site.register(ServiceItem)