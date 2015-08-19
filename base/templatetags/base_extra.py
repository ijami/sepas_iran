__author__ = 'MJR'

from django import template


register = template.Library()

@register.filter()
def get_cart_num(user):
    return user.get_cart_num()

@register.filter()
def range(num):
    x = []
    for i in range(num):
        x.append(i)
    return x