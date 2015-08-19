from django.http.response import HttpResponse
from django.views.generic.edit import FormView

from management.forms import AdvertiseForm
from management.models import AdvertiseBox
from sepas_iran.settings import SITE_URL

__author__ = 'po0ya'


class AdvertiseView(FormView):
    template_name = 'management/advertisement.html'
    form_class = AdvertiseForm
    success_url = SITE_URL

    def form_valid(self, form):
        data = form.cleaned_data
        adds = [('add{}'.format(i - 1), data.get('add{}'.format(i), '')) for i in range(1, 6)]
        print(adds)
        for index, add in adds:
            AdvertiseBox.load().set_add(index, add)
        print('cheeeel')
        print(str(AdvertiseBox.load()))
        return HttpResponse('success')

    def get_initial(self):
        adv = AdvertiseBox.load()
        adds = [('add{}'.format(i + 1), getattr(adv, 'add{}'.format(i)).name if getattr(adv, 'add{}'.format(i)) else '')
                for i in range(0, 5)]
        return dict(adds)
