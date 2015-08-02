from django.forms.models import ModelForm
from tourist.models import Tourist

__author__ = 'mohsenkatebi'
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class MyUserCreationForm(UserCreationForm):
    firstname = forms.CharField(max_length=100, label="نام", required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'نام'}))
    lastname = forms.CharField(max_length=100, label="نام خانوادگی", required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'نام خانوادگی'}))
    username = forms.CharField(max_length=100, label="نام کاربری", required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'نام کاربری'}))
    email = forms.EmailField(max_length=100, label="پست الکترونیک", required=True,
                             widget=forms.EmailInput(attrs={'placeholder': 'example@host.com'}))
    password1 = forms.CharField(max_length=100, label="گذرواژه", required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'گذرواژه'}))
    password2 = forms.CharField(max_length=100, label="تکرار گذرواژه", required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'تکرار گذرواژه'}))

    class Meta:
        model = User
        fields = ("firstname", "lastname", "username", "email")

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(("نام کاربری موجود است. یک نام کاربری دیگر انتخاب کنید."))

    def clean_email(self):
        email = self.cleaned_data["email"]
        if email == "":
            raise forms.ValidationError("ایمیل معتبر نیست.")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1", "")
        password2 = self.cleaned_data["password2"]
        if password1 != password2:
            raise forms.ValidationError(("گذرواژه ها همخوانی ندارند."))
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class TouristEditProfileForm(ModelForm):
    firstname = forms.CharField(max_length=100, label="نام", required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'نام'}))
    lastname = forms.CharField(max_length=100, label="نام خانوادگی", required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'نام خانوادگی'}))
    username = forms.CharField(max_length=100, label="نام کاربری", required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'نام کاربری', 'readonly': 'readonly'}))
    email = forms.EmailField(max_length=100, label="پست الکترونیک", required=True,
                             widget=forms.EmailInput(attrs={'placeholder': 'example@host.com', 'readonly': 'readonly'}))
    image = forms.ImageField()
    birth_day = forms.DateField(widget=forms.DateInput)
    city = forms.CharField()
    address = forms.CharField(max_length=1000)

    def __init__(self, instance=None):
        self.instance = instance
        self.firstname = instance.primary_user.first_name
        self.lastname = instance.primary_user.last_name
        self.username = instance.primary_user.username
        self.email = instance.primary_user.email
        self.image = instance.image
        self.city = instance.location.city
        self.address = instance.location.address

    class Meta:
        model = Tourist
        fields = ['birth_day', 'image', 'telephone']

    def save(self, commit=True):
        super(TouristEditProfileForm, self).save()