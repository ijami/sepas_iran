__author__ = 'MJR'
from tourist.forms import PersianDateField
from django.forms.models import ModelForm
from service.models import Tour, Room, Flight
from django import forms
from base.models import City
from service_provider.models import ServiceProvider, Hotel, TravelAgency, AirLine
import datetime


# class TourForm(ModelForm):
#
#     origin = forms.CharField(max_length=100)
#     destination = forms.CharField(max_length=100)
#     going_date = forms.DateField()
#     return_date = forms.DateField()
#     description = forms.CharField(widget=forms.Textarea)
#     hotel_name = forms.CharField(max_length=140)
#     capacity = forms.IntegerField()
#     image = forms.ImageField(widget=forms.FileInput(attrs={'id': 'file_upload'}))
#     price = forms.IntegerField()
#     tag_line = forms.CharField()
#
#
#
#     def __init__(self, user, *args, **kwargs):
#         super(TourForm, self).__init__(*args, **kwargs)
#         self.provider = user
#
#     class Meta:
#         model = Tour
#         fields = ['image']
#
#
#     def save(self, commit=True):
#         instance = Tour()
#         instance.description = self['description'].value()
#         instance.return_date = self['return_date'].value()
#         instance.going_date = self['going_date'].value()
#         instance.hotel_name = self['hotel_name'].value()
#         c = City.objects.filter(name=self['origin'].value())
#         if len(c) != 0:
#             instance.origin = c[0]
#         else:
#             d = City(name=self['origin'].value())
#             d.save()
#             instance.origin = d
#         e = City.objects.filter(name=self['destination'].value())
#         if len(e) != 0:
#             instance.destination = e[0]
#         else:
#             f = City(name=self['destination'].value())
#             f.save()
#             instance.destination = f
#         instance.capacity = self['capacity']
#         instance.price = self['price']
#         instance.tag_line = self['tag_line']
#         if self['image'].value() != None:
#             instance.image = self.provider.image
#         else:
#             instance.image = self.provider.image
#         instance.travel_agency = self.provider
#         instance.sold_number = 't' + str(self.provider.id) + str(len(Tour.objects.filter(travel_agency=self.provider)))
#         print(instance)
#         instance.save()

class TourForm(ModelForm):

    origin = forms.ModelChoiceField(queryset=City.objects.all(), label="مبدا", required=True,
                                  error_messages={'required': "پر کردن فیلد مبدا لزامی است"})
    destination = forms.ModelChoiceField(queryset=City.objects.all(), label="مقصد", required=True,
                                  error_messages={'required': "پر کردن فیلد مقصد الزامی است"})
    going_date = PersianDateField(label="تاریخ رفت", required=True,
                                 error_messages={'required': "پر کردن فیلد تاریخ رفت الزامی است"},
                                 widget=forms.DateInput(attrs={'class': 'datepicker'}))
    return_date = PersianDateField(label="تاریخ بازگشت", required=True,
                                 error_messages={'required': "پر کردن فیلد تاریخ برگشت الزامی است"},
                                 widget=forms.DateInput(attrs={'class': 'datepicker'}))
    description = forms.CharField(max_length=500, label="توضیحات", required=False,
                              error_messages={'required': "پر کردن فیلد توضیحات الزامی است"},
                              widget=forms.Textarea(attrs={'placeholder': 'توضیحات اضافی درباره تور و امکانات و مشخصات آن', 'rows': '8'}))
    hotel_name = forms.CharField(max_length=200, label="نام هتل", required=False)
    capacity = forms.IntegerField(max_value=2000, label="ظرفیت", required=True, error_messages={'required': 'پر کردن فیلد ظرفیت الزامی است'})
    image = forms.ImageField(widget=forms.FileInput(attrs={'id': 'file-upload'}), required=False)
    price = forms.IntegerField(max_value=500000000, label="قیمت هر نفر بر حسب ریال", required=True, error_messages={'required': 'پر کردن فیلد قیمت الزامی است'})
    tag_line = forms.CharField(max_length=555, label="جمله نشانه", required=True,
                                error_messages={'required': "پر کردن فیلد جمله نشانه الزامی است"},
                                widget=forms.TimeInput(attrs={'placeholder': 'مثال: تور خاطره انگیز در سواحل بکر دریای مازندران'}))
    CHOICES = (
        ("plane", "هواپیما"),
        ("tran", "قطار"),
        ("bus", 'اتوبوس'),
    )
    trans_type = forms.ChoiceField(label="وسیله نقلیه", required=True, error_messages={'required': "پرکردن فیلد وسیله نقلیه الزامی است"}
                                   , choices=CHOICES)

    def clean_going_date(self):
        going_date = self.cleaned_data["going_date"]
        now = datetime.datetime.now().date()
        if going_date < now:
            raise forms.ValidationError(message="تاریخ رفت وارد شده، معتبر نیست.", code='invalid going_date')
        return going_date

    def clean_return_date(self):
        return_date = self.cleaned_data["return_date"]
        going_date = self.cleaned_data['going_date']
        if going_date >= return_date:
            print("borde shodim")
            raise forms.ValidationError(message="تاریخ برگشت وارد شده، معتبر نیست.", code='invalid return_date')
        return return_date

    def clean_capacity(self):
        capacity = self.cleaned_data['capacity']
        if capacity < 1:
            raise forms.ValidationError(message="ظرفیت  باید عددی مثبت باشد", code="non positive capacity")
        return capacity

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0 or price > 500000000:
            raise forms.ValidationError(message="قیمت معقول نیست", code="bad price")
        return price



    class Meta:
        model = Tour
        fields = ['image']


    def save(self, commit=True, user=None):
        service = super(TourForm, self).save(commit=False)
        service.travel_agency = user
        service.price = self.cleaned_data['price']
        service.capacity = self.cleaned_data['capacity']
        service.sold_number = 't_' + str(user.id) + "_" + str(len(Tour.objects.filter(travel_agency=user)))
        service.tag_line = self.cleaned_data['tag_line']
        service.trans_type = self.cleaned_data['trans_type']
        print("sag")
        print(self.cleaned_data['image'])
        service.image = self.cleaned_data['image']
        if service.image == None:
            service.image = user.image
        service.origin = self.cleaned_data['origin']
        service.destination = self.cleaned_data['destination']
        service.going_date = self.cleaned_data['going_date']
        service.return_date = self.cleaned_data['return_date']
        service.description = self.cleaned_data['description']
        service.hotel_name = self.cleaned_data['hotel_name']
        if commit:
            service.save()
        else:
            return service


class RoomForm(ModelForm):

    start_date = PersianDateField(label="تاریخ شروع", required=True,
                                 error_messages={'required': "پر کردن فیلد تاریخ شروغ الزامی است"},
                                 widget=forms.DateInput(attrs={'class': 'datepicker'}))
    end_date = PersianDateField(label="تاریخ پایان", required=True,
                                 error_messages={'required': "پر کردن فیلد تاریخ پایان الزامی است"},
                                 widget=forms.DateInput(attrs={'class': 'datepicker'}))
    description = forms.CharField(max_length=500, label="توضیحات", required=False,
                              error_messages={'required': "پر کردن فیلد توضیحات الزامی است"},
                              widget=forms.Textarea(attrs={'placeholder': 'توضیحات اضافی درباره تور و امکانات و مشخصات آن', 'rows': '8'}))

    capacity = forms.IntegerField(max_value=2000, label="تعداد اتاق ها", required=True, error_messages={'required': 'پر کردن فیلد ظرفیت الزامی است'})
    image = forms.ImageField(widget=forms.FileInput(attrs={'id': 'file-upload'}), required=False)
    price = forms.IntegerField(max_value=500000000, label="قیمت اتاق", required=True, error_messages={'required': 'پر کردن فیلد قیمت الزامی است'})
    tag_line = forms.CharField(max_length=555, label="جمله نشانه", required=True,
                                error_messages={'required': "پر کردن فیلد جمله نشانه الزامی است"},
                                widget=forms.TimeInput(attrs={'placeholder': 'مثال: تور خاطره انگیز در سواحل بکر دریای مازندران'}))
    number_of_bed = forms.IntegerField(max_value=8, required=True, label="تعداد تخت", error_messages={"required": "پرکردن فیلد تعداد اتاق الزامی است"})
    has_television = forms.BooleanField(widget=forms.CheckboxInput, label="تلویزیون", required=False)
    has_telephone = forms.BooleanField(widget=forms.CheckboxInput, label="تلفن", required=False)

    class Meta:
        model = Room
        fields = ['image']

    def clean_start_date(self):
        start_date = self.cleaned_data["start_date"]
        now = datetime.datetime.now().date()
        if start_date < now:
            raise forms.ValidationError(message="تاریخ شروع وارد شده، معتبر نیست.", code='invalid start_date')
        return start_date

    def clean_end_date(self):
        end_date = self.cleaned_data["end_date"]
        start_date = self.cleaned_data['start_date']
        if start_date >= end_date:
            raise forms.ValidationError(message="تاریخ اتمام وارد شده، معتبر نیست.", code='invalid end_date')
        return end_date

    def clean_capacity(self):
        capacity = self.cleaned_data['capacity']
        if capacity < 1:
            raise forms.ValidationError(message="ظرفیت  باید عددی مثبت باشد", code="non positive capacity")
        return capacity

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0 or price > 500000000:
            raise forms.ValidationError(message="قیمت معقول نیست", code="bad price")
        return price

    def clean_number_of_bed(self):
        capacity = self.cleaned_data['number_of_bed']
        if capacity < 1:
            raise forms.ValidationError(message="تعداد تخت باید عددی مثبت باشد", code="non positive bed number")
        return capacity

    def save(self, commit=True, user=None):
        r = super(RoomForm, self).save(commit=False)
        r.hotel = user
        r.number_of_bed = self.cleaned_data['number_of_bed']
        r.has_telephone = self.cleaned_data['has_telephone']
        r.has_television = self.cleaned_data['has_television']
        r.price = self.cleaned_data['price']
        r.capacity = self.cleaned_data['capacity']
        r.tag_line = self.cleaned_data['tag_line']
        r.description = self.cleaned_data['description']
        r.start_date = self.cleaned_data['start_date']
        r.end_date = self.cleaned_data['end_date']
        if self.cleaned_data['image']:
            r.image = self.cleaned_data['image']
        else:
            r.image = user.image
        r.sold_number = 'r_' + str(user.id) + "_" + str(len(Room.objects.filter(hotel=user)))
        if commit:
            r.save()
        else:
            return r

class FlightForm(ModelForm):

    origin = forms.ModelChoiceField(queryset=City.objects.all(), label="مبدا", required=True,
                                  error_messages={'required': "پر کردن فیلد مبدا لزامی است"})
    destination = forms.ModelChoiceField(queryset=City.objects.all(), label="مقصد", required=True,
                                  error_messages={'required': "پر کردن فیلد مقصد الزامی است"})
    date = PersianDateField(label="تاریخ پرواز", required=True,
                                 error_messages={'required': "پر کردن فیلد تاریخ پرواز الزامی است"},
                                 widget=forms.DateInput(attrs={'class': 'datepicker'}))
    description = forms.CharField(max_length=500, label="توضیحات", required=False,
                              error_messages={'required': "پر کردن فیلد توضیحات الزامی است"},
                              widget=forms.Textarea(attrs={'placeholder': 'توضیحات اضافی درباره تور و امکانات و مشخصات آن', 'rows': '8'}))
    capacity = forms.IntegerField(max_value=2000, label="ظرفیت", required=True, error_messages={'required': 'پر کردن فیلد ظرفیت الزامی است'})
    image = forms.ImageField(widget=forms.FileInput(attrs={'id': 'file-upload'}), required=False)
    price = forms.IntegerField(max_value=500000000, label="قیمت هر نفر بر حسب ریال", required=True, error_messages={'required': 'پر کردن فیلد قیمت الزامی است'})
    tag_line = forms.CharField(max_length=555, label="جمله نشانه", required=True,
                                error_messages={'required': "پر کردن فیلد جمله نشانه الزامی است"},
                                widget=forms.TimeInput(attrs={'placeholder': 'مثال: تور خاطره انگیز در سواحل بکر دریای مازندران'}))
    time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'), label="ساعت پرواز", required=True, error_messages={"required": "پرکردن فیلد ساعت پرواز الزامی است",
                                        "invalid": "ساعت پرواز معتبر نیست"       })
    flight_number = forms.CharField(max_length=20, label= "شماره پرواز",required=True, error_messages={'required': 'وارد کردن فیلد شماره پرواز الزامی است'})
    airplane = forms.CharField(max_length=40, label="نوع هواپیما", required=True, error_messages={"required": "پرکردن فیلد نوع هواپیما الزامی است"})

    class Meta:
        model = Flight
        fields = ['image']

    def clean_capacity(self):
        capacity = self.cleaned_data['capacity']
        if capacity < 1:
            raise forms.ValidationError(message="ظرفیت باید عددی مثبت باشد")
        return capacity

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0 or price > 1000000000:
            raise forms.ValidationError(message="قیمت نامعتبر است")
        return price

    def save(self, commit=True, user=None):
        flight = super(FlightForm, self).save(commit=False)
        flight.airline = user
        flight.origin = self.cleaned_data['origin']
        flight.destination = self.cleaned_data['destination']
        flight.capacity = self.cleaned_data['capacity']
        flight.price = self.cleaned_data['price']
        print(flight.price)
        flight.tag_line = self.cleaned_data['tag_line']
        flight.date = self.cleaned_data['date']
        flight.time = self.cleaned_data['time']
        flight.airplane = self.cleaned_data['airplane']
        flight.flight_number = self.cleaned_data['flight_number']
        flight.sold_number = 'f_' + str(user.id) + "_" + str(len(Flight.objects.filter(airline=user)))
        if self.cleaned_data['image'] != None:
            flight.image = self.cleaned_data['image']
        else:
            flight.image = user.image
        if commit:
            flight.save()
        else:
            return flight


class CapacityAddingForm(forms.Form):
    added_capacity = forms.IntegerField(min_value=1, max_value=200, required=True, label="افزایش ظرفیت درخواستی")
    sold_number = forms.CharField(max_length=20, required=False)

class SearchServiceListForm(forms.Form):
    price_range = forms.CharField(max_length=30, label="قیمت",
    widget=forms.TextInput(attrs={'type': 'text', 'id':'amount' , 'style': 'border:0; color:#777777; padding:12; font-size:15px; width: 220px; '}))

    service_provider = forms.ModelChoiceField(queryset=ServiceProvider.objects.all(), label='گردشساز: ', required=False)
    travel_agency = forms.ModelChoiceField(queryset=TravelAgency.objects.all(), required=False)
    hotel = forms.ModelChoiceField(queryset=Hotel.objects.all(), required=False)
    airline = forms.ModelChoiceField(queryset=AirLine.objects.all(), required=False)
    start_date = PersianDateField(label="از تاریخ:", widget= forms.DateInput(attrs={'class': 'datepicker ui input'}), required=False)
    end_date = PersianDateField(label="تا تاریخ:", widget= forms.DateInput(attrs={'class': 'datepicker ui input'}), required=False)
    origin = forms.ModelChoiceField(queryset=City.objects.all(), label="مبدا: ", required=False)
    destination = forms.ModelChoiceField(queryset=City.objects.all(), label="مقصد: ", required=False)
    location = forms.ModelChoiceField(queryset=City.objects.all(), label="مکان: ", required=False)