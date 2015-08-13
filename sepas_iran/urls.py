from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'base.views.home_view.home', name='home'),
    url(r'^accounts/login/$', 'base.views.login_view.login_user', name='login'),
    url(r'^accounts/forgot-password/$', 'base.views.forgot_pass_view.forgot_pass', name='forgot-password'),
    url(r'^accounts/logout/$', 'base.views.login_view.logout_user', name='logout'),
    url(r'^service/', include('service.urls')),
    url(r'^tourist/', include('tourist.urls')),
    url(r'^manage/', include('management.urls')),
    url(r'^sale/', include('sale.urls')),
    url(r'^messaging/', include('messaging.urls')),
    url(r'^service_provider/', include('service_provider.urls')),
    url(r'^admin/', include(admin.site.urls)),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
