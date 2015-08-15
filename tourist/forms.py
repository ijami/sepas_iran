from django.forms.models import ModelForm
from django import forms
from django.contrib.auth.models import User

from base.models import City, Location
from sale.models import Cart
from tourist.models import Tourist
from jdatetime import date as jdate
import datetime
import re


class PersianDateField(forms.DateField):
    default_error_messages = {
        'invalid': "لطفا یک تاریخ معتبر وارد کنید",
    }

    def to_python(self, value):
        print(value)
        date_regex = re.compile('^(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)$')
        test = date_regex.match(value)
        if test:
            jyear = int(test.group('year'))
            jmonth = int(test.group('month'))
            jday = int(test.group('day'))

            try:
                python_date = jdate(jyear, jmonth, jday).togregorian()
                return python_date
            except Exception:
                raise forms.ValidationError(self.default_error_messages['invalid'], code='invalid')
        else:
            raise forms.ValidationError(self.default_error_messages['invalid'], code='invalid')


class TouristCreationForm(ModelForm):
    first_name = forms.CharField(max_length=100, label="نام", required=True,
                                 error_messages={'required': "پر کردن فیلد نام الزامی است"},
                                 widget=forms.TextInput(attrs={'placeholder': 'نام'}))
    last_name = forms.CharField(max_length=100, label="نام خانوادگی", required=True,
                                error_messages={'required': "پر کردن فیلد نام خانوادگی الزامی است"},
                                widget=forms.TextInput(attrs={'placeholder': 'نام خانوادگی'}))
    username = forms.CharField(max_length=100, label="نام کاربری", required=True,
                               error_messages={'required': "پر کردن فیلد نام کاربری الزامی است"},
                               widget=forms.TextInput(attrs={'placeholder': 'نام کاربری'}))
    email = forms.EmailField(max_length=100, label="پست الکترونیک", required=True,
                             error_messages={'required': "پر کردن فیلد پست الکترونیک الزامی است"},
                             widget=forms.EmailInput(attrs={'placeholder': 'example@host.com'}))
    password1 = forms.CharField(max_length=100, label="گذرواژه", required=True,
                                error_messages={'required': "پر کردن فیلد گذرواژه الزامی است"},
                                widget=forms.PasswordInput(attrs={'placeholder': 'گذرواژه'}))
    password2 = forms.CharField(max_length=100, label="تکرار گذرواژه", required=True,
                                error_messages={'required': "پر کردن فیلد تکرار گذرواژه الزامی است"},
                                widget=forms.PasswordInput(attrs={'placeholder': 'تکرار گذرواژه'}))
    telephone = forms.CharField(max_length=20, label="شماره تلفن همراه", required=True,
                                error_messages={'required': "پر کردن فیلد شماره تلفن الزامی است"},
                                widget=forms.TimeInput(attrs={'placeholder': '09121234567'}))
    birth_day = PersianDateField(label="تاریخ تولد", required=True,
                                 error_messages={'required': "پر کردن فیلد تولد الزامی است"},
                                 widget=forms.DateInput(attrs={'class': 'datepicker'}))
    city = forms.ModelChoiceField(queryset=City.objects.all(), label="شهر", required=False,
                                  error_messages={'required': "پر کردن فیلد شهر الزامی است"})

    address = forms.CharField(max_length=500, label="آدرس", required=False,
                              error_messages={'required': "پر کردن فیلد آدرس الزامی است"},
                              widget=forms.Textarea(attrs={'placeholder': 'آدرس کامل', 'rows': '5'}))

    class Meta:
        model = Tourist
        fields = ('telephone', 'birth_day')

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            if re.match('^\w+$', username):
                return username
            else:
                raise forms.ValidationError("نام کابری فقط میتواند از حروف لاتین، عدد و کاراکتر _ تشکیل شود.",
                                            code="bad_format")
        raise forms.ValidationError("این نام کاربری موجود است. یک نام کاربری دیگر انتخاب کنید.", code='duplicate_user')

    def clean_email(self):
        email = self.cleaned_data["email"]
        if email == "":
            raise forms.ValidationError("ایمیل معتبر نیست.")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1", "")
        password2 = self.cleaned_data["password2"]
        if password1 != password2:
            raise forms.ValidationError("گذرواژه ها همخوانی ندارند.")
        return password2

    def clean_birth_day(self):
        birthday = self.cleaned_data["birth_day"]
        now = datetime.datetime.now().date()
        min_date = datetime.date(year=1900, month=1, day=1)
        if birthday > now or birthday < min_date:
            raise forms.ValidationError(message="تاریخ تولد وارد شده، معتبر نیست.", code='invalid birhtday')
        return birthday

    def clean_telephone(self):
        number = self.cleaned_data['telephone']
        if re.match('^\d{11,13}$', number):
            return number
        else:
            raise forms.ValidationError("شماره موبایل وارد شده معتبر نیست", code="invalid mobile number")

    def save(self, commit=True):
        tourist = super(TouristCreationForm, self).save(commit=False)
        user = User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data["email"],
                                        password=self.cleaned_data["password1"])
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.save()
        tourist.primary_user = user
        location = Location(city=self.cleaned_data["city"], address=self.cleaned_data["address"])
        location.save()
        cart = Cart()
        cart.save()
        tourist.location = location
        tourist.cart = cart
        if commit:
            tourist.save()
        return tourist


class TouristEditProfileForm(ModelForm):
    firstname = forms.CharField(max_length=100, label="نام", required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'نام'}))
    lastname = forms.CharField(max_length=100, label="نام خانوادگی", required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'نام خانوادگی'}))
    username = forms.CharField(max_length=100, label="نام کاربری", required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'نام کاربری', 'readonly': 'readonly'}))
    birth_day = forms.DateField(widget=forms.DateInput())
    city = forms.CharField()
    address = forms.CharField(max_length=1000)
    telephone = forms.CharField(max_length=20)
    image = forms.ImageField(widget=forms.FileInput(attrs={'class' : 'ui inverted button'}))

    def __init__(self, *args, instance=None, **kwargs):
        super(TouristEditProfileForm, self).__init__(*args, **kwargs)
        self.instance = instance
        if instance:
            self.fields['firstname'].initial = instance.primary_user.first_name
            self.fields['lastname'].initial = instance.primary_user.last_name
            self.fields['username'].initial = instance.primary_user.username
            self.fields['birth_day'].initial = instance.birth_day
            self.fields['city'].initial = instance.location.city
            self.fields['address'].initial = instance.location.address
            self.fields['telephone'].initial = instance.telephone
            self.fields['image'].inital = instance.image

    class Meta:
        model = Tourist
        fields = ['birth_day', 'telephone', 'image']

    def save(self, commit=True):
        tourist = User.objects.get(username=self['username'].value()).site_user.tourist
        tourist.primary_user.first_name = self['firstname'].value()
        tourist.primary_user.last_name = self['lastname'].value()
        tourist.primary_user.save()
        tourist.birth_day = self['birth_day'].value()
        tourist.location.address = self['address'].value()
        tourist.location.save()
        tourist.telephone = self['telephone'].value()
        if self['image'].value() != None:
            tourist.image = self['image'].value()
        tourist.save()
