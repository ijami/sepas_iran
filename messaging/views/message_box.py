from base.views.decorators import login_required
from django.db.models.query_utils import Q
from messaging.models import Message
from django.shortcuts import render

__author__ = 'Mohsen'


@login_required
def message_box_view (request):
    if request.method == 'GET':
        usern = request.user.site_user

        messages = Message.objects.filter(Q(sender=usern) | Q(receiver=usern))


        return render(request, 'messaging/message_box.html', {
            'messages': messages,
            'user': usern
        })
