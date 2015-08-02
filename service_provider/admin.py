from django.contrib import admin

# Register your models here.
from service_provider.models import AirLine, Hotel, TravelAgency

admin.site.register(AirLine)
admin.site.register(Hotel)
admin.site.register(TravelAgency)

