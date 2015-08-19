__author__ = 'Ehsan and MJR!'
from django.conf.urls import url

urlpatterns = [
    # Examples:
    url(r'^panel/$', 'service_provider.views.panel_view.panel', name='service_provider_panel'),
    url(r'^panel/new_service$', 'service_provider.views.new_service.new_service', name='new_service'),
    url(r'^register/$', 'service_provider.views.register_view.register', name='register_service_provider'),
    url(r'^panel/service_list/$', 'service_provider.views.service_list.service_list', name='provider_service_list'),
    url(r'^panel/service_list/capa', 'service_provider.views.service_list.add_capacity', name='add_service_capacity'),
    url(r'^panel/ads$', 'service_provider.views.ad_request.advertisement_request', name='ads'),
    url(r'information/(\d+)$', 'service_provider.views.information.information', name='sag')
]
