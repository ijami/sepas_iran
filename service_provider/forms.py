# from django.forms.models import ModelForm
import datetime
import re

from django import forms
from django.contrib.auth.models import User
from django.forms.models import ModelForm
from django.template.defaultfilters import register

from jdatetime import date as jdate

from base.models import City, Location
from service_provider.models import ServiceProvider, TravelAgency, Hotel, AirLine


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
                                        error_messages={'required': "پر کردن فیلد توضیح مختصر اجباری است"},
                                        widget=forms.TextInput(
                                            attrs={'placeholder': 'برای مثال: اولین شرکت خدمات جامع گردشگری ایران'}))
    long_description = forms.CharField(max_length=100, label="توضیح بلند", required=False,
                                       error_messages={'required': "پر کردن فیلد توضیح بلند اجباری است"},
                                       widget=forms.Textarea(attrs={
                                           'placeholder': 'توضیحاتی در مورد سابقه و خدمات ارائه شده توسط گردش ساز / یار',
                                           'rows': '5'}))
    image = forms.ImageField(label="عکس پروفایل کاربری", required=False,
                             widget=forms.FileInput(attrs={'style': "display:none", 'accept': "image/*"}))
    national_id = forms.IntegerField(min_value=0, max_value=10000000000, label="کد ملی", required=False,
                                     error_messages={'required': "پر کردن فیلد کد ملی الزامی است"},
                                     widget=forms.NumberInput(attrs={'placeholder': '0015557890'}))
    address = forms.CharField(max_length=500, label="آدرس", required=False,
                              error_messages={'required': "پر کردن فیلد آدرس الزامی است"},
                              widget=forms.Textarea(attrs={'placeholder': 'آدرس کامل', 'rows': '5'}))
    types = (('tour', "tour"),
             ('hotel', "hotel"),
             ('airline', "airline"),
             )
    type = forms.ChoiceField(required=True, label="خدمت ارائه شده توسط شرکت", widget=forms.HiddenInput, choices=types,
                             error_messages={'required': "انتخاب نوع سرویس الزامی است",
                                             'invalid_choice': "انتخاب نوع سرویس الزامی است"})

    # hotel
    degree = forms.IntegerField(label="درجه هتل", required=False,
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
    map_widget = forms.CharField(max_length=500, required=False, label="موقعیت جغرافیایی",
                                 widget=forms.TextInput(
                                     attrs={'placeholder': "https://www.google.com/maps/place/...", 'dir': 'ltr'}))
    ###Airline
    is_international = forms.BooleanField(required=False, label="دارای پروازهای بین المللی")

    ###tour

    class Meta:
        model = ServiceProvider
        fields = ('name', 'short_description', 'long_description', 'image', 'telephone')

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
        temp = super(ServiceProviderCreationForm, self).save(commit=False)
        service_type = self.cleaned_data.get('type')
        if service_type == 'tour':
            service_provider = TravelAgency()
            user = User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data["email"],
                                            password=self.cleaned_data["password1"])
            user.first_name = self.cleaned_data["first_name"]
            user.last_name = self.cleaned_data["last_name"]
            user.save()
            service_provider.primary_user = user
            location = Location(city=self.cleaned_data["city"], address=self.cleaned_data["address"])
            location.save()
            service_provider.location = location
            service_provider.image = temp.image
            service_provider.telephone = temp.telephone
            service_provider.name = temp.name
            service_provider.short_description = temp.short_description
            service_provider.long_description = temp.long_description
        elif service_type == 'hotel':
            service_provider = Hotel()
            user = User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data["email"],
                                            password=self.cleaned_data["password1"])
            user.first_name = self.cleaned_data["first_name"]
            user.last_name = self.cleaned_data["last_name"]
            user.save()
            service_provider.primary_user = user
            location = Location(city=self.cleaned_data["city"], address=self.cleaned_data["address"])
            location.save()
            service_provider.location = location
            service_provider.image = temp.image
            service_provider.telephone = temp.telephone
            service_provider.name = temp.name
            service_provider.short_description = temp.short_description
            service_provider.long_description = temp.long_description
            service_provider.has_coffeeshop = self.cleaned_data["has_coffeeshop"]
            service_provider.has_conference_hall = self.cleaned_data["has_conference_hall"]
            service_provider.has_emergency = self.cleaned_data["has_emergency"]
            service_provider.has_fire_extinguisher = self.cleaned_data["has_fire_extinguisher"]
            service_provider.has_health_center = self.cleaned_data["has_health_center"]
            service_provider.has_gamenet = self.cleaned_data["has_gamenet"]
            service_provider.has_jungle = self.cleaned_data["has_jungle"]
            service_provider.has_internet = self.cleaned_data["has_internet"]
            service_provider.has_pool = self.cleaned_data["has_pool"]
            service_provider.has_sport_salloon = self.cleaned_data["has_sport_salloon"]
            service_provider.has_parking = self.cleaned_data["has_parking"]
            service_provider.has_shop_center = self.cleaned_data["has_shop_center"]
            service_provider.has_restaurant = self.cleaned_data["has_restaurant"]
            service_provider.has_protection_system = self.cleaned_data["has_protection_system"]
            service_provider.has_photo_studio = self.cleaned_data["has_photo_studio"]
            service_provider.has = self.cleaned_data["has_restaurant"]

        elif service_type == 'airline':
            service_provider = AirLine()
            user = User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data["email"],
                                            password=self.cleaned_data["password1"])
            user.first_name = self.cleaned_data["first_name"]
            user.last_name = self.cleaned_data["last_name"]
            user.save()
            service_provider.primary_user = user
            location = Location(city=self.cleaned_data["city"], address=self.cleaned_data["address"])
            location.save()
            service_provider.location = location
            service_provider.image = temp.image
            service_provider.telephone = temp.telephone
            service_provider.name = temp.name
            service_provider.short_description = temp.short_description
            service_provider.long_description = temp.long_description
            service_provider.is_international = self.cleaned_data["is_international"]
        if commit:
            service_provider.save()
        return service_provider
