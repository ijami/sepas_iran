from django.shortcuts import render
from django.views.generic.edit import FormView

from management.forms import IntervalReportForm

__author__ = 'Iman'


class IntervalReportView(FormView):
    template_name = 'management/area_report.html'
    form_class = IntervalReportForm

    def form_valid(self, form):
        data = form.cleaned_data
        start_date = data['start_date']
        end_date = data['end_date']
        service = data['service']
        kind = data['kind']
        return render(self.request, 'management/area_report.html', {'form': form})


class PieReportView(FormView):
    template_name = 'management/pie_report.html'
    form_class = IntervalReportForm

    def form_valid(self, form):
        return render(self.request, 'management/pie_report.html', {'form': form})
