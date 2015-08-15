__author__ = 'MJR'

from django.forms import ModelForm
from service.models import Tour, TourLocation, Room, Flight
from django import forms
from base.models import City


class TourForm(ModelForm):

    origin = forms.CharField(max_length=100)
    destination = forms.CharField(max_length=100)
    going_date = forms.DateField()
    return_date = forms.DateField()
    description = forms.TextInput()
    hotel_name = forms.CharField(max_length=140)
    capacity = forms.IntegerField()
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'ui inverted button'}))
    price = forms.IntegerField()
    tag_line = forms.CharField()



    def __init__(self, user, *args, **kwargs):
        super(TourForm, self).__init__(*args, **kwargs)
        self.provider = user

    class Meta:
        model = Tour
        fields = ['image']

    def save(self, commit=True):
        instance = Tour()
        instance.capacity = self.capacity
        instance.description = self.description
        instance.return_date = self.return_date
        instance.going_date = self.going_date
        instance.hotel_name = self.hotel_name
        instance.origin = TourLocation(city=City(name=self.origin))
        instance.destination = TourLocation(city=City(name=self.destination))
        instance.capacity = self.capacity
        instance.price = self.price
        instance.tag_line = self.tag_line
        if self.image:
            instance.image = self.image
        else:
            instance.image = self.provider.image
        instance.travel_agency = self.provider
        instance.sold_number = 't' + str(self.provider.id) + len(Tour.objects.filter(travel_agency=self.provider))
        instance.save()


class RoomForm(ModelForm):

    class Meta:
        model = Room
        fields = ['has_television']

class FlightForm(ModelForm):

    class Meta:
        model = Flight
        fields = ['flight_number']