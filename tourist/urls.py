__author__ = 'Ehsan'

from django.conf.urls import include, url
from django.views.generic.base import TemplateView

urlpatterns = [
    # Examples:
    url(r'^financeReport/$', TemplateView.as_view(template_name='tourist/userFinanceReport.html'), name='user_finance_report'),
    url(r'^panel$', TemplateView.as_view(template_name='tourist/panel.html'), name='panel'),
    url(r'^register/$', 'tourist.views.singup_view.register', name='register_tourist'),
    url(r'^forgot-password/$', 'tourist.views.forgot_pass_view.forgot_pass', name='forgot-password'),
    url(r'^logout/$', 'tourist.views.login_view.logout_view', name='logout_tourist'),
]
