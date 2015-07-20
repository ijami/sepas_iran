from django.conf.urls import url
from django.views.generic.base import TemplateView

__author__ = 'Iman'
urlpatterns = [
    # Examples:
    url(r'^list$', TemplateView.as_view(template_name='service_list.html'), name='service-list'),
]
