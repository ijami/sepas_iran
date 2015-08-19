from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render

from sale.views.finance import provided_services_count,saled_services_count,waited_services_count,income
from tourist.views.crm_function import feedback_count


@login_required
def reprot_view(request):
    if request.method == 'GET':
        service_provider = request.user.site_user

        if service_provider:
            context = {
                'provided_services': provided_services_count(service_provider),
                'saled_services': saled_services_count(service_provider),
                'waited_services': waited_services_count(service_provider),
                'income' : income(service_provider),
                'feedback_count' : feedback_count(service_provider),
            }
            return render(request, 'service_provider/report_provider.html', context)
        return HttpResponse("You don't have permition to this page")
