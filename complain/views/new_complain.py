from django.core.urlresolvers import reverse
from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.views.generic.base import View

__author__ = 'Iman'

class NewComplain(View):

    def get(self, request):
        return redirect(reverse('service_list'))

    def post(self, request):
        item_id = self.request.POST['service_item_id']
        title = self.request.POST['title']
        text = self.request.POST['text']
        print(title)
        print(text)
        print(item_id)
        return HttpResponse("salam")