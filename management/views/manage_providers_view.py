from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.views.generic.base import View
from service_provider.models import ServiceProvider

__author__ = 'Iman'

class NewProviders(View):
    template_name = 'management/new_providers.html'

    def get(self, request):
        providers = ServiceProvider.objects.filter(is_verified=False)
        return render(self.request, self.template_name, {'providers': providers})

    def post(self, request):
        provider_id = self.request.POST['provider_id']
        provider = ServiceProvider.objects.get(id=provider_id)
        provider.is_verified = True
        provider.save()
        return redirect(reverse('new_providers'))

class ActiveProviders(View):
    template_name = 'management/active_providers.html'

    def get(self, request):
        providers = ServiceProvider.objects.filter(is_verified=True, is_active=True)
        # print(providers)
        return render(self.request, self.template_name, {'providers': providers})

    def post(self, request):
        provider_id = self.request.POST['provider_id']
        provider = ServiceProvider.objects.get(id=provider_id)
        provider.is_active = False
        provider.save()
        return redirect(reverse('active_providers'))


class DeactiveProviders(View):
    template_name = 'management/deactive_providers.html'

    def get(self, request):
        providers = ServiceProvider.objects.filter(is_verified=True, is_active=False)
        # print(providers)
        return render(self.request, self.template_name, {'providers': providers})

    def post(self, request):
        provider_id = self.request.POST['provider_id']
        provider = ServiceProvider.objects.get(id=provider_id)
        provider.is_active = True
        provider.save()
        return redirect(reverse('deactive_providers'))