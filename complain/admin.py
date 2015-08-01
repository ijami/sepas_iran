from django.contrib import admin

# Register your models here.
from complain.models import RoomPoll, FlightPoll, TourPoll, Complain

admin.site.register(RoomPoll)
admin.site.register(FlightPoll)
admin.site.register(TourPoll)
admin.site.register(Complain)