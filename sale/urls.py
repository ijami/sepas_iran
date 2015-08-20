__author__ = 'Javad'

from django.conf.urls import url
from django.views.generic.base import TemplateView

__author__ = 'Iman'
urlpatterns = [
    # Examples:
    url(r'^cart$', 'sale.views.cart_view.cart_view', name='cart'),
    url(r'^success$', 'sale.views.success_view.success_view', name='success'),
    url(r'^shopping$', TemplateView.as_view(template_name='sale/service.html'), name='shopping'),
    url(r'^service/([rtf]_\d+_\d+)$', 'sale.views.service.service_show', name='service'),
    url(r'^comment$', 'sale.views.comment.add_comment', name='comment'),
    url(r'add_to_cart$', 'sale.views.add_to_cart.add_to_cart', name='add_to_cart'),
    url(r'^cart/([rtf]_\d+_\d+)$', 'sale.views.add_to_cart.delete', name='delete_item'),
    url(r'^buy$', 'sale.views.buy.buy', name='buy'),
    url(r'^bank$', 'sale.views.buy.bank', name='bank'),
]
