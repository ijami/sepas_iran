__author__ = 'Ehsan'
from django.conf.urls import url

urlpatterns = [
    url(r'^register/$', 'service_provider.views.register_view.register', name='register_service_provider')
]
