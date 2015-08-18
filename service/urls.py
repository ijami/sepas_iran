from django.conf.urls import url
from django.views.generic.base import TemplateView

__author__ = 'Iman'
urlpatterns = [
    # Examples:
    url(r'^(?P<type>tour|hotel|flight)/$', 'service.views.service_view.show_type_service_list_view', name='type_service_list'),
    url(r'^$', 'service.views.service_view.show_service_list_view', name='service_list'),

]
