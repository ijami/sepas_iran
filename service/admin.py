from django.contrib import admin

# Register your models here.
from service.models import Flight, Room, Tour, Airport, Comment


class CommentInline(admin.TabularInline):
    model = Comment


class FlightAdmin(admin.ModelAdmin):
    inlines = [CommentInline]


class RoomAdmin(admin.ModelAdmin):
    inlines = [CommentInline]


class TourAdmin(admin.ModelAdmin):
    inlines = [CommentInline]

admin.site.register(Flight, FlightAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Tour, TourAdmin)
admin.site.register(Airport)