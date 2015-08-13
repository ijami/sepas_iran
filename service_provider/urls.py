__author__ = 'MJR'
from django.conf.urls import url
from django.views.generic.base import TemplateView


urlpatterns = [
    # Examples:
    url(r'^panel/$', 'service_provider.views.panel_view.panel'),
]
