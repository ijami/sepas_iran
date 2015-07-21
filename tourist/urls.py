__author__ = 'Ehsan'

from django.conf.urls import include, url

urlpatterns = [
    # Examples:
    url(r'^register/$', 'tourist.views.singup_view.register', name='home')
]
