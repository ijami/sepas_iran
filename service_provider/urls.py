__author__ = 'Ehsan and MJR!'
from django.conf.urls import url

urlpatterns = [
    url(r'^register/$', 'service_provider.views.register_view.register', name='register_service_provider'),
    url(r'^panel/$', 'service_provider.views.panel_view.panel', name='service_provider_panel')
]
