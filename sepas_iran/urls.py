from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'sepas_iran.views.home', name='home'),
    url(r'^service/', include('service.urls')),
    url(r'^tourist/', include('tourist.urls')),
    url(r'^manage/', include('management.urls')),
    url(r'^sale/', include('sale.urls')),
    url(r'^messaging/', include('messaging.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
