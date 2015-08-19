from django import forms

__author__ = 'po0ya'


class AdvertiseForm(forms.Form):
    add1 = forms.CharField(label='تبلیغ اول', required=False)
    add2 = forms.CharField(label='تبلیغ دوم', required=False)
    add3 = forms.CharField(label='تبلیغ سوم', required=False)
    add4 = forms.CharField(label='تبلیغ چهارم', required=False)
    add5 = forms.CharField(label='تبلیغ پنجم', required=False)