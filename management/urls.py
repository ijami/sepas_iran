from management.views.advertise_select import AdvertiseView

__author__ = 'Iman'
from django.conf.urls import url
from django.views.generic.base import TemplateView
from .views import advertise_search

urlpatterns = [
    # Examples:
    url(r'^finance$', TemplateView.as_view(template_name='management/financeReport.html'), name='finance'),
    url(r'^advertisement$', AdvertiseView.as_view(), name='advertisement'),
    url(r'^service_activate$', TemplateView.as_view(template_name='management/service_activate.html'),
        name='service-activate'),
    url(r'^service_provider_activate$', TemplateView.as_view(template_name='management/service_provider_activate.html'),
        name='service-provider-activate'),
    url(r'^buy_report', TemplateView.as_view(template_name='management/buy_report.html'), name='buy_report'),
    url(r'^sell_report', TemplateView.as_view(template_name='management/advertisement.html'), name='sell_report'),
    url(r'^$', TemplateView.as_view(template_name='management/dashboard.html'), name='management_dashboard'),
    url(r'^search/$', advertise_search.search, name='search_advertise')
]
