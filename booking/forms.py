from django import forms
from .models import Booking
from teams.models import Team

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['team', 'date', 'start_time', 'end_time']

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'start_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'end_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'team': forms.Select(attrs={'class': 'form-select'}),
        }
