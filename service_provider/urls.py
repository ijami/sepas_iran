__author__ = 'MJR'
from django.conf.urls import url
from django.views.generic.base import TemplateView


urlpatterns = [
    # Examples:
    url(r'^panel/$', 'service_provider.views.panel_view.panel', name='service_provider_panel'),
    url(r'^panel/new_service$', 'service_provider.views.new_service.new_service', name='new_service'),
]
