from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic.base import View
from complain.models import Complain
from sale.models import ServiceItem

__author__ = 'Iman'

class NewComplain(View):

    def get(self, request):
        return redirect(reverse('service_list'))

    def post(self, request):
        item_id_text = self.request.POST['service_item_id']
        item_id = int(item_id_text.split('_')[1])
        title = self.request.POST['title']
        text = self.request.POST['text']
        service_item = ServiceItem.objects.get(id=item_id)
        Complain.objects.create(title=title, text=text, service_item=service_item)
        return redirect(reverse('service_list'))
