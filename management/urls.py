__author__ = 'Iman'
from django.conf.urls import url
from django.views.generic.base import TemplateView

__author__ = 'Iman'
urlpatterns = [
    # Examples:
    url(r'^$', TemplateView.as_view(template_name='management/dashboard.html'), name='service-list'),
]
