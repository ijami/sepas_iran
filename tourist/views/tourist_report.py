from django.contrib.auth.decorators import login_required
from django.conf import settings
__author__ = 'آرمان'

from django.shortcuts import render
from sepas_iran.tourist.models import Tourist
from django.http import Http404
from sepas_iran.service_provider.models import ServiceProvider

# Create your views here.

@login_required
def tourist_report(user_id):
    try:
        tourist = Tourist.objects.get(id=user_id)
    except Tourist.DoesNotExist:
        return Http404

    report = tourist.boughtservice_set
# download pdf of report

