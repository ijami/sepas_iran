from sepas_iran import settings

__author__ = 'Ehsan'

from django.conf.urls import url
from django.views.generic.base import TemplateView

urlpatterns = [
    # Examples:
    url(r'^financeReport/$', TemplateView.as_view(template_name='tourist/userFinanceReport.html'), name='user_finance_report'),
    url(r'^panel$', 'tourist.views.profile_view.profile_view', name='panel'),
    url(r'^panel/modify$', TemplateView.as_view(template_name='tourist/profile_modify.html'), name='profile_modify'),
    url(r'^register/$', 'tourist.views.singup_view.register', name='register_tourist'),
    url(r'^report$', TemplateView.as_view(template_name='tourist/report.html'), name='report'),
    url(r'^service_list$', TemplateView.as_view(template_name='tourist/services.html'), name='service_list'),
]


