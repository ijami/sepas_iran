from complain.views.new_complain import NewComplain

__author__ = 'Iman'

from django.conf.urls import url

urlpatterns = [
    # Examples:
    url(r'^new', NewComplain.as_view(), name='new_complain'),
]