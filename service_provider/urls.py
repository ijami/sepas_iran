__author__ = 'Ehsan and MJR!'
from django.conf.urls import url

urlpatterns = [
    # Examples:
    url(r'^panel/$', 'service_provider.views.panel_view.panel', name='service_provider_panel'),
    url(r'^panel/new_service$', 'service_provider.views.new_service.new_service', name='new_service'),
    url(r'^register/$', 'service_provider.views.register_view.register', name='register_service_provider'),
]
