from django.contrib import admin

# Register your models here.
from base.models import SiteUser, City

admin.site.register(SiteUser)
admin.site.register(City)