__author__ = 'Javad'

from django.conf.urls import url
from django.views.generic.base import TemplateView

urlpatterns = [
    # Examples:
    url(r'^message_box$', TemplateView.as_view(template_name='messaging/message_box.html'), name='message_box'),
    url(r'^new_message$', TemplateView.as_view(template_name='messaging/write.html'), name='write')
]
