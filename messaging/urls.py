__author__ = 'Javad'

from django.conf.urls import include, url
from django.views.generic.base import TemplateView

urlpatterns = [
    # Examples:
    url(r'^message_box$', 'messaging.view.message_box.message_box_view', name='message_box'),
    url(r'^new_message$', login_required(TemplateView.as_view(template_name='messaging/write.html'), name='write')
]
