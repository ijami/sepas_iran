from django.contrib import admin

# Register your models here.
from messaging.models import Message

admin.site.register(Message)