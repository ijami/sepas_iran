from management.views.advertise_select import AdvertiseView
from management.views.complains import UnAnsweredComplainList, AnsweredComplainList, AnswerComplain
from management.views.manage_providers_view import NewProviders, ActiveProviders, DeactiveProviders
from management.views.report_view import IntervalReportView, PieReportView, MapReportView

__author__ = 'Iman'
from django.conf.urls import url
from django.views.generic.base import TemplateView
from base.views.decorators import manager_required
from .views import advertise_search

urlpatterns = [
    # Examples:
    url(r'^finance$', manager_required(TemplateView.as_view(template_name='management/financeReport.html')),
        name='finance'),
    url(r'^advertisement$', manager_required(AdvertiseView.as_view()), name='advertisement'),
    url(r'^service_activate$', manager_required(TemplateView.as_view(template_name='management/service_activate.html')),
        name='service-activate'),
    url(r'^service_provider_activate$',
        manager_required(TemplateView.as_view(template_name='management/manage_providers.html')),
        name='service-provider-activate'),
    url(r'^unanswered_complain', manager_required(UnAnsweredComplainList.as_view()), name='unanswered_complains'),
    url(r'^answered_complain', manager_required(AnsweredComplainList.as_view()), name='answered_complains'),
    url(r'^answer', manager_required(AnswerComplain.as_view()), name='answer_complain'),
    url(r'^area_report', manager_required(IntervalReportView.as_view()), name='area_report'),
    url(r'^pie_report', manager_required(PieReportView.as_view()), name='pie_report'),
    url(r'^map_report', manager_required(MapReportView.as_view()), name='map_report'),
    url(r'^new_providers', manager_required(NewProviders.as_view()), name='new_providers'),
    url(r'^active_providers', manager_required(ActiveProviders.as_view()), name='active_providers'),
    url(r'^deactive_providers', manager_required(DeactiveProviders.as_view()), name='deactive_providers'),
    url(r'^sell_report', manager_required(TemplateView.as_view(template_name='management/advertisement.html')),
        name='sell_report'),
    url(r'^$', manager_required(TemplateView.as_view(template_name='management/dashboard.html')),
        name='management_dashboard'),
    url(r'^search/$', advertise_search.search, name='search_advertise'),
]
