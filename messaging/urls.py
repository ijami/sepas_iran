from django.contrib.auth.decorators import login_required

__author__ = 'Javad'

from django.conf.urls import url
from django.views.generic.base import TemplateView

urlpatterns = [
    # Examples:
    url(r'^tourist/message_box$', 'messaging.views.message_box.tourist_message_box_view', name='tourist_message_box'),
    url(r'^tourist/new_message$', 'messaging.views.write_message.tourist_new_message_view', name='tourist_write'),
    url(r'^service_provider/message_box$', 'messaging.views.message_box.service_provider_message_box_view', name='service_provider_message_box'),
    url(r'^service_provider/new_message$', 'messaging.views.write_message.service_provider_new_message_view', name='service_provider_write'),
    url(r'^manager/message_box$', 'messaging.views.message_box.manager_message_box_view', name='manager_message_box'),
    url(r'^manager/new_message$', 'messaging.views.write_message.manager_new_message_view', name='manager_write')
]
