from django import forms
from .models import Team
from django.contrib.auth.models import User

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'captain']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter team name'
            }),
            'captain': forms.Select(attrs={
                'class': 'form-select',
            }),
        }

        labels = {
            'name': 'Team Name',
            'captain': 'Select Captain',
        }
