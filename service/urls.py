from django.conf.urls import url
from django.views.generic.base import TemplateView

__author__ = 'Iman'
urlpatterns = [
    # Examples:
    url(r'^(?P<type>tour|room|flight)/$', 'service.views.service_view.show_type_service_list_view', name='type_service_list'),
    url(r'^information/([rtf]_\d+_\d+)$', 'service.views.information.information', name='buyers'),
]
