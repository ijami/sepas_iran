from django.db import models

# Create your models here.
from base.models import SiteUser


class Message(models.Model):
    text = models.TextField()
    sender = models.ForeignKey(SiteUser, related_name='sent_messages')
    receiver = models.ForeignKey(SiteUser, related_name='received_messages')
    is_read = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender.primary_user.username + ": " + self.text