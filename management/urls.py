__author__ = 'آرمان'
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'sepas_iran.views.home', name='home'),
    url(r'^service/', include('service.urls')),
    url(r'^management/', include('management.urls')),
    url(r'^admin/', include(admin.site.urls)),
]