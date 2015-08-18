# from django.forms.models import ModelForm
import datetime
import re

from django import forms
from django.contrib.auth.models import User
from django.forms.models import ModelForm
from django.template.defaultfilters import register

from jdatetime import date as jdate
from location_field.forms.plain import PlainLocationField

from base.models import City, Location
from sale.models import Cart
from service_provider.models import ServiceProvider


@register.filter(is_safe=True)
def label_with_classes(value, arg):
    return value.label_tag(attrs={'class': arg})


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


class ServiceProviderCreationForm(ModelForm):
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
    city = forms.ModelChoiceField(queryset=City.objects.all(), label="شهر", required=False,
                                  error_messages={'required': "پر کردن فیلد شهر الزامی است"})
    name = forms.CharField(max_length=100, label="نام شرکت", required=True,
                           error_messages={'required': "پر کردن فیلد نام شرکت الزامی است"},
                           widget=forms.TextInput(attrs={'placeholder': 'نام شرکت'}))
    short_description = forms.CharField(max_length=100, label="توضیح مختصر", required=True,
                                        error_messages={'required': "برای مثال: اولین شرکت خدمات جامع گردشگری ایران"},
                                        widget=forms.TextInput(attrs={'placeholder': 'توضیح مختصر'}))
    long_description = forms.CharField(max_length=100, label="توضیح بلند", required=False,
                                       error_messages={'required': "پر کردن فیلد توضیح بلند اجباری است"},
                                       widget=forms.Textarea(attrs={
                                           'placeholder': 'توضیحاتی در مورد سابقه و خدمات ارائه شده توسط گردش ساز / یار',
                                           'rows': '5'}))
    image = forms.ImageField(label="عکس پروفایل کاربری", required=False,
                             widget=forms.FileInput(attrs={'style': "display:none", 'accept': "image/*"}))
    advertise_image = forms.ImageField(label="عکس برای بنر تبلیغاتی", required=False,
                                       widget=forms.FileInput(attrs={'style': "display:none", 'accept': "image/*"}))
    national_id = forms.IntegerField(min_value=0, max_value=10000000000, label="کد ملی", required=False,
                                     error_messages={'required': "پر کردن فیلد کد ملی الزامی است"},
                                     widget=forms.NumberInput(attrs={'placeholder': '0015557890'}))
    address = forms.CharField(max_length=500, label="آدرس", required=False,
                              error_messages={'required': "پر کردن فیلد آدرس الزامی است"},
                              widget=forms.Textarea(attrs={'placeholder': 'آدرس کامل', 'rows': '5'}))

    # hotel
    map_widget = forms.CharField(max_length=500)
    degree = forms.IntegerField(label="درجه هتل", required=True,
                                error_messages={'required': "پر کردن فیلد درجه هتل الزامی است"},
                                widget=forms.NumberInput(attrs={'hidden': "hidden"}))
    has_restaurant = forms.BooleanField(required=False, label="رستوران")
    has_parking = forms.BooleanField(required=False, label="پارکینگ")
    has_internet = forms.BooleanField(required=False, label="اینترنت")
    has_pool = forms.BooleanField(required=False, label="استخر")
    has_conference_hall = forms.BooleanField(required=False, label="اتاق کنفرانس")
    has_fire_extinguisher = forms.BooleanField(required=False, label="سیستم اطفای حریق")
    has_sport_salloon = forms.BooleanField(required=False, label="سالن ورزشی")
    has_health_center = forms.BooleanField(required=False, label="مرکز بهداشت")
    has_coffeeshop = forms.BooleanField(required=False, label="کافی شاپ")
    has_emergency = forms.BooleanField(required=False, label="اورژانس")
    has_jungle = forms.BooleanField(required=False, label="فضای سبز")
    has_protection_system = forms.BooleanField(required=False, label="سیستم امنیتی")
    has_shop_center = forms.BooleanField(required=False, label="مرکز خرید")
    has_gamenet = forms.BooleanField(required=False, label="گیم نت")
    has_photo_studio = forms.BooleanField(required=False, label="آتلیه عکاسی")

    ###Airline


    ###tour

    class Meta:
        model = ServiceProvider
        fields = ('advertise_image', 'name', 'short_description', 'long_description', 'advertise_image', 'image')

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
        tourist = super(ServiceProviderCreationForm, self).save(commit=False)
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
