__author__ = 'MJR'
from tourist.forms import PersianDateField
from django.forms.models import ModelForm
from service.models import Tour, Room, Flight
from django import forms
from base.models import City
from django.forms import widgets


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
                              widget=forms.Textarea(attrs={'placeholder': 'توضیحات اضافی درباره امکانات تور', 'rows': '5'}))
    hotel_name = forms.CharField(max_length=200, label="نام هتل", required=False)
    capacity = forms.IntegerField(max_value=2000, label="ظرفیت", )
    image = forms.ImageField(widget=forms.FileInput(attrs={'id': 'file-upload'}), required=False)
    price = forms.IntegerField(max_value=10000000, label="قیمت هر نفر بر حسب ریال")
    tag_line = forms.CharField(max_length=555, label="جمله نشانه", required=True,
                                error_messages={'required': "پر کردن فیلد جمله نشانه الزامی است"},
                                widget=forms.TimeInput(attrs={'placeholder': '09121234567'}))

    class Meta:
        model = Tour
        fields = ['image']


    def save(self, commit=True, user=None):
        service = super(TourForm, self).save(commit=False)
        service.travel_agency = user
        service.price = self.cleaned_data['price']
        service.capacity = self.cleaned_data['capacity']
        service.sold_number = 1
        service.tag_line = self.cleaned_data['tag_line']
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

    capacity = forms.IntegerField()
    number_of_bed = forms.IntegerField()
    image = forms.ImageField(widget=forms.FileInput(attrs={'id': 'file_upload'}))
    price = forms.IntegerField()
    tag_line = forms.CharField()
    has_television = forms.BooleanField()
    has_telephone = forms.BooleanField()

    class Meta:
        model = Room
        fields = ['image']

    def __init__(self, user, *args, **kwargs):
        super(TourForm, self).__init__(*args, **kwargs)
        self.provider = user

    def save(self, commit=True):
        r = Room()
        r.hotel = self.provider
        r.number_of_bed = self.number_of_bed
        r.has_telephone = self.has_telephone
        r.has_television = self.has_television
        r.price = self.price
        r.capacity = self.capacity
        r.tag_line = self.tag_line
        if self.image:
            r.image = self.image
        else:
            r.image = self.provider.image
        r.sold_number = 'r' + str(self.provider.id) + len(Tour.objects.filter(travel_agency=self.provider))
        r.save()


class FlightForm(ModelForm):

    class Meta:
        model = Flight
        fields = ['image']