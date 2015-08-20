from _ast import Set
from datetime import timedelta
from django.shortcuts import render
from django.views.generic.edit import FormView
import jdatetime
from base.models import City
from management.forms import IntervalReportForm,PieReportForm,MapReportForm

from sale.views.finance import dashboard_report
from service.models import Tour, Flight

__author__ = 'Iman'


class IntervalReportView(FormView):
    template_name = 'management/area_report.html'
    form_class = IntervalReportForm

    def form_valid(self, form):
        data = form.cleaned_data
        start_date = data['start_date']
        end_date = data['end_date']
        service = data['service']
        kind = int(data['kind'])
        service_list = dashboard_report(start_date, end_date, int(service))
        day_count = (end_date - start_date).days + 1
        chart_values = []
        for single_date in (start_date + timedelta(n) for n in range(day_count)):
            val = 0
            for x in service_list:
                if x.service.get_date() == single_date:
                    print(x.service.get_date())
                    print(jdatetime.date.fromgregorian(date=x.service.get_date()).strftime("%Y/%m/%d"))
                    if kind == 2:
                        val += x.number
                    else:
                        val += x.number * x.service.price
            chart_values.append([jdatetime.datetime.fromgregorian(date=single_date).strftime("%Y/%m/%d"), val])

        return render(self.request, 'management/area_report.html', {'form': form, 'values': chart_values, 'kind': kind})


class PieReportView(FormView):
    template_name = 'management/pie_report.html'
    form_class = PieReportForm

    def form_valid(self, form):
        data = form.cleaned_data
        start_date = data['start_date']
        end_date = data['end_date']
        kind = int(data['kind'])
        service_item_list = dashboard_report(start_date, end_date, 30)
        values = {'tour': 0, 'flight': 0, 'hotel': 0}
        for item in service_item_list:
            key = 'hotel'
            if type(item.service) == Tour:
                key = 'tour'
            elif type(item.service) == Flight:
                key = 'flight'

            if kind == 2:
                values[key] += item.number
            else:
                values[key] += item.number * item.service.price

        return render(self.request, 'management/pie_report.html', {'form': form,
                                                                   'tour': values['tour'],
                                                                   'flight': values['flight'],
                                                                   'hotel': values['hotel']})


class MapReportView(FormView):
    template_name = 'management/map_report.html'
    form_class = MapReportForm

    def form_valid(self, form):
        data = form.cleaned_data
        start_date = data['start_date']
        end_date = data['end_date']
        service_item_list = dashboard_report(start_date, end_date, 30)
        city_value = {}
        for city in City.objects.all():
            city_value[city.map_code] = 0
        for item in service_item_list:
            city_value[item.service.get_city().map_code] += item.number

        return render(self.request, 'management/map_report.html', {'form': form,
                                                                   'city_val': city_value})