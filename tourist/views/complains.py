from django.views.generic.list import ListView
from complain.models import Complain

__author__ = 'Iman'


class ComplainList(ListView):
    template_name = 'tourist/complain_list.html'
    model = Complain
    context_object_name = 'complains_list'

    def get_queryset(self):
        return Complain.objects.filter(service_item__factor__tourist=self.request.user.site_user).all()