from django.contrib.auth.decorators import login_required
from messaging.models import Message
__author__ = 'Mohsen'

from django.shortcuts import render

@login_required
def message_box_view (request):
    if request.method == 'GET':
        user = request.user.site_user

        message_sent = Message.objects.filter(sender=user)
        message_received = Message.objects.filter(receiver=user)

        return render(request, 'messaging/message_box.html', {
            'message_sent': message_sent,
            'message_received': message_received,
            'user': user
        })

