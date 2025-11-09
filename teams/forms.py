# teams/forms.py
from django import forms
from .models import Team, Player

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'age', 'position', 'contact']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'min': 8}),
            'position': forms.Select(attrs={'class': 'form-select'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
        }

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'captain', 'members']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'captain': forms.Select(attrs={'class': 'form-select'}),
            'members': forms.CheckboxSelectMultiple(),
        }
