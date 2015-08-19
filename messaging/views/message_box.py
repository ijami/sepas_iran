from django.http import HttpResponse
from base.views.decorators import login_required
from django.db.models.query_utils import Q
from messaging.models import Message
from django.shortcuts import render

__author__ = 'Mohsen'


@login_required
def message_box_view (request):
    if request.method == 'GET':
        usern = request.user.site_user

        messages = Message.objects.filter(Q(sender=usern) | Q(receiver=usern)).order_by('-create_date')

        new_messages = messages.filter(is_read=False).all()

        read_messages = list(messages.filter(is_read=True).all())

        for message in new_messages:
            if message.receiver == usern:
                message.is_read = True
                message.save()

        return render(request, 'messaging/message_box.html', {
            'read_messages': read_messages,
            'new_messages': new_messages,
            'user': usern
        })

