__author__ = 'Javad'

from django.conf.urls import url
from django.views.generic.base import TemplateView

__author__ = 'Iman'
urlpatterns = [
    # Examples:
    url(r'^cart$', TemplateView.as_view(template_name='sale/cart.html'), name='cart'),
    url(r'^shopping$', TemplateView.as_view(template_name='sale/service.html'), name='shopping'),
]
