__author__ = 'MJR'
from django.shortcuts import render, redirect
from django.conf import settings
from django.template import RequestContext


def panel(request):
    user = request.user.site_user
    context = user.get_fields()
    data = {'context': context}
    return render(request, 'panel.html', data, context_instance=RequestContext(request))

