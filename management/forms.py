from django.forms.fields import ChoiceField
from django.forms.forms import Form, ValidationError
from django.forms.widgets import DateInput
from service_provider.forms import PersianDateField
from django import forms

__author__ = 'Iman'


class AdvertiseForm(forms.Form):
    add1 = forms.CharField(label='تبلیغ اول', required=False)
    add2 = forms.CharField(label='تبلیغ دوم', required=False)
    add3 = forms.CharField(label='تبلیغ سوم', required=False)
    add4 = forms.CharField(label='تبلیغ چهارم', required=False)
    add5 = forms.CharField(label='تبلیغ پنجم', required=False)
class IntervalReportForm(Form):
    start_date = PersianDateField(label='شروع بازه', required=True,
                                  error_messages={'required': 'پر کزدن فیلد شروع بازه الزامیست!'},
                                  widget=DateInput(attrs={'class': 'datepicker'}),)
    end_date = PersianDateField(label='پایان بازه', required=True,
                                error_messages={'required':'پر کردن فیلد پایان بازه الزامیست!'},
                                widget=DateInput(attrs={'class': 'datepicker'}),)
    service = ChoiceField(choices=((30, 'همه‌‌ی خدمات'), (2, 'تور'), (3, 'هواپیما'), (5, 'هتل' ),), label='انتخاب خدمات')
    kind = ChoiceField(choices=((1, 'مبلغ دریافتی'), (2, 'تعداد فروخته شده')), label='بر حسب')

    def clean(self):
        data = self.cleaned_data
        start_date = data['start_date']
        end_date = data['end_date']
        if start_date > end_date:
            raise ValidationError(message='تاریخ‌های وارد شده معتبر نیست')


class PieReportForm(Form):
    start_date = PersianDateField(label='شروع بازه', required=True,
                                  error_messages={'required': 'پر کزدن فیلد شروع بازه الزامیست!'},
                                  widget=DateInput(attrs={'class': 'datepicker'}),)
    end_date = PersianDateField(label='پایان بازه', required=True,
                                error_messages={'required':'پر کردن فیلد پایان بازه الزامیست!'},
                                widget=DateInput(attrs={'class': 'datepicker'}),)
    kind = ChoiceField(choices=((1, 'مبلغ دریافتی'), (2, 'تعداد فروخته شده')), label='بر حسب')

    def clean(self):
        data = self.cleaned_data
        start_date = data['start_date']
        end_date = data['end_date']
        if start_date > end_date:
            raise ValidationError(message='تاریخ‌های وارد شده معتبر نیست')

class MapReportForm(Form):
    start_date = PersianDateField(label='شروع بازه', required=True,
                                  error_messages={'required': 'پر کزدن فیلد شروع بازه الزامیست!'},
                                  widget=DateInput(attrs={'class': 'datepicker'}),)
    end_date = PersianDateField(label='پایان بازه', required=True,
                                error_messages={'required':'پر کردن فیلد پایان بازه الزامیست!'},
                                widget=DateInput(attrs={'class': 'datepicker'}),)

    def clean(self):
        data = self.cleaned_data
        start_date = data['start_date']
        end_date = data['end_date']
        if start_date > end_date:
            raise ValidationError(message='تاریخ‌های وارد شده معتبر نیست')