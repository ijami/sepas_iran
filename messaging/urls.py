from django.contrib.auth.decorators import login_required

__author__ = 'Javad'

from django.conf.urls import url
from django.views.generic.base import TemplateView

urlpatterns = [
    # Examples:
    url(r'^message_box$', 'messaging.views.message_box.message_box_view', name='message_box'),
    url(r'^new_message$', 'messaging.views.write_message.new_message_view', name='write')
]
