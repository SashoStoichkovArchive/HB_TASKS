from django import forms
from . import models


class FlightForm(forms.ModelForm):
    class Meta:
        model = models.Flight
        fields = '__all__'