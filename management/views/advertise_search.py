from django.contrib.sessions.serializers import JSONSerializer
from django.core import serializers
from django.http.response import HttpResponse
import json
from service_provider.models import ServiceProvider
from base.views.decorators import manager_required
__author__ = 'po0ya'


class Model(ServiceProvider):
    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
        }

@manager_required()
def search(request):
    name = request.POST.get('name', 'bad request')
    service_providers = [s.name for s in ServiceProvider.objects.filter(name__icontains=name)]
    return HttpResponse(json.dumps(service_providers))
