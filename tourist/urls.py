__author__ = 'Ehsan'

from django.conf.urls import include, url
from django.views.generic.base import TemplateView

urlpatterns = [
    # Examples:
    url(r'^register/$', 'tourist.views.singup_view.register', name='home'),
    url(r'^financeReport/$', TemplateView.as_view(template_name='tourist/userFinanceReport.html'), name='user_finance_report')
]
