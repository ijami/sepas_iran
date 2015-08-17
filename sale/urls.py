__author__ = 'Javad'

from django.conf.urls import url
from django.views.generic.base import TemplateView

__author__ = 'Iman'
urlpatterns = [
    # Examples:
    url(r'^cart$', 'sale.views.cart_view.cart_view', name='cart'),
<<<<<<< HEAD
    url(r'^success$', 'sale.views.success_view.success_view', name='success'),
    url(r'^shopping$', TemplateView.as_view(template_name='sale/service.html'), name='shopping'),
=======
    url(r'^service/([rtf]_[\d+]_[\d+])$', 'sale.views.service.service_show', name='service'),
>>>>>>> 2e23deb83af3cbccb335ee348f7b91c0ef3a2df1
]
