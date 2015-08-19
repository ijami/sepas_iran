__author__ = 'Javad'

from django.conf.urls import url
from django.views.generic.base import TemplateView
from base.views.decorators import login_required

urlpatterns = [
    # Examples:
    url(r'^message_box$', login_required(TemplateView.as_view(template_name='messaging/message_box.html')),
        name='message_box'),
    url(r'^new_message$', login_required(TemplateView.as_view(template_name='messaging/write.html')), name='write')
]
