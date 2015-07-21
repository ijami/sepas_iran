__author__ = 'Iman'
from django.conf.urls import url
from django.views.generic.base import TemplateView

__author__ = 'Iman'
urlpatterns = [
    # Examples:
    url(r'^finance$', TemplateView.as_view(template_name='management/financeReport.html'), name='finance'),
    url(r'^advertisement$', TemplateView.as_view(template_name='management/advertisement.html'), name='advertisement'),
    url(r'^service_activate$', TemplateView.as_view(template_name='management/service_activate.html'),
        name='service-activate'),
    url(r'^service_provider_activate$', TemplateView.as_view(template_name='management/service_provider_activate.html'),
        name='service-provider-list'),
    url(r'^buy_report', TemplateView.as_view(template_name='management/buy_report.html'), name='buy_report'),
    url(r'^sell_report', TemplateView.as_view(template_name='management/advertisement.html'), name='sell_report'),
    url(r'^$', TemplateView.as_view(template_name='management/dashboard.html'), name='service-list')
]
