__author__ = 'Iman'
from django.conf.urls import url
from django.views.generic.base import TemplateView

__author__ = 'Iman'
urlpatterns = [
    # Examples:

    url(r'^finance$', TemplateView.as_view(template_name='management/financeReport.html'), name='service-list'),
    url(r'^advertisement$', TemplateView.as_view(template_name='management/advertisement.html'), name='service-list'),
    url(r'^service_activate$', TemplateView.as_view(template_name='management/service_activate.html'), name='service-list'),
    url(r'^$', TemplateView.as_view(template_name='management/dashboard.html'), name='service-list'),
]
