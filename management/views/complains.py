from django.core.urlresolvers import reverse
from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.views.generic.base import View
from django.views.generic.list import ListView
from complain.models import Complain

__author__ = 'Iman'

class UnAnsweredComplainList(ListView):
    template_name = 'management/un_answered_complains.html'
    model = Complain
    context_object_name = 'complains_list'

    def get_queryset(self):
        return Complain.objects.filter(state='Q').all()


class AnsweredComplainList(ListView):
    template_name = 'management/answered_complains.html'
    model = Complain
    context_object_name = 'complains_list'

    def get_queryset(self):
        return Complain.objects.filter(state='F').all()


class AnswerComplain(View):
    def post(self, request):
        text = self.request.POST['text']
        complain_id = int(self.request.POST['complain_id'].split('_')[1])
        print(complain_id)
        print(text)
        complain = Complain.objects.get(id=complain_id)
        complain.answer = text
        complain.state = 'F'
        complain.save()
        return redirect(reverse('unanswered_complains'))
