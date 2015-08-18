from management.views.report_view import IntervalReportView, PieReportView, MapReportView

__author__ = 'Iman'
from django.conf.urls import url
from django.views.generic.base import TemplateView

urlpatterns = [
    # Examples:
    url(r'^finance$', TemplateView.as_view(template_name='management/financeReport.html'), name='finance'),
    url(r'^advertisement$', TemplateView.as_view(template_name='management/advertisement.html'), name='advertisement'),
    url(r'^service_activate$', TemplateView.as_view(template_name='management/service_activate.html'),
        name='service-activate'),
    url(r'^service_provider_activate$', TemplateView.as_view(template_name='management/service_provider_activate.html'),
        name='service-provider-activate'),
    url(r'^area_report', IntervalReportView.as_view(), name='area_report'),
    url(r'^pie_report', PieReportView.as_view(), name='pie_report'),
    url(r'^map_report', MapReportView.as_view(), name='map_report'),
    url(r'^sell_report', TemplateView.as_view(template_name='management/advertisement.html'), name='sell_report'),
    url(r'^chart', TemplateView.as_view(template_name='management/chart.html')),
    url(r'^$', TemplateView.as_view(template_name='management/dashboard.html'), name='management_dashboard'),
]
