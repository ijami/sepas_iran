from django.contrib import admin

# Register your models here.
from base.models import SiteUser, City, Location, CityCollection



admin.site.register(SiteUser)
admin.site.register(City)
admin.site.register(Location)
admin.site.register(CityCollection)
