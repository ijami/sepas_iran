from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import FormView
from management.forms import IntervalReportForm

__author__ = 'Iman'


class IntervalReportView(FormView):
    template_name = 'management/buy_report.html'
    form_class = IntervalReportForm

    def form_valid(self, form):
        data = form.cleaned_data
        start_date = data['start_date']
        end_date = data['end_date']
        render('management/buy_report.html', {'form': form})
