from sepas_iran import settings
from tourist.views.complains import ComplainList

__author__ = 'Ehsan'

from django.conf.urls import url
from django.views.generic.base import TemplateView
from base.views.decorators import tourist_required

urlpatterns = [
    # Examples:
    url(r'^financeReport/$', tourist_required(TemplateView.as_view(template_name='tourist/userFinanceReport.html')),
        name='user_finance_report'),
    url(r'^panel$', 'tourist.views.profile_view.profile_view', name='panel'),
    url(r'^panel/modify$', 'tourist.views.prifile_edit_view.profile_edit_view', name='profile_modify'),
    url(r'^panel/modify/upload_image$', 'tourist.views.prifile_edit_view.profile_edit_view', name='upload_image'),
    url(r'^register/$', 'tourist.views.register_view.register', name='register_tourist'),
    url(r'^report$', 'tourist.views.report_view.reprot_view', name='report'),
    url(r'^service_list$', 'tourist.views.service_list.service_list', name='service_list'),
    url(r'^complains', ComplainList.as_view(), name='tourist_complains'),
    url(r'^information/(\d+)$', 'tourist.views.profile_view.information', name='tourist_information')
]
