from django.forms.fields import ChoiceField
from django.forms.forms import Form, ValidationError
from django.forms.widgets import DateInput
from service_provider.forms import PersianDateField

__author__ = 'Iman'

class IntervalReportForm(Form):
    start_date = PersianDateField(label='شروع بازه', required=True,
                                  error_messages={'required': 'پر کزدن فیلد شروع بازه الزامیست!'},
                                  widget=DateInput(attrs={'class': 'datepicker'}),)
    end_date = PersianDateField(label='پایان بازه', required=True,
                                error_messages={'required':'پر کردن فیلد پایان بازه الزامیست!'},
                                widget=DateInput(attrs={'class': 'datepicker'}),)
    service = ChoiceField(choices=((1, 'همه‌‌ی خدمات'), (2, 'تور'), (3, 'هواپیما'), (4, 'هتل' ),), label='انتخاب خدمات')

    kind = ChoiceField(choices=((1, 'مبلغ دریافتی'), (2, 'تعداد فروخته شده')), label='بر حسب')

    def clean(self):
        data = self.cleaned_data
        start_date = data['start_date']
        end_date = data['end_date']
        if start_date > end_date:
            print("inja")
            raise ValidationError(message='تاریخ‌های وارد شده معتبر نیست')

