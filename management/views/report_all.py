__author__ = 'آرمان'
from django.shortcuts import render
from sepas_iran.tourist.models import Tourist
from django.http import Http404
from sepas_iran.service.models import ServiceInfo
from sepas_iran.service_provider.models import ServiceProvider



def all_report():
    tourists = Tourist.objects.all()
    service_providers = ServiceProvider.objects.all()

    tourist_reports = [tourist.boughtservice_set for tourist in tourists]
    service_provider_reports = [service_info.boughtservice_set for service_info in service_providers.serviceinfo_set]

    reports = tourist_reports | service_provider_reports
