from django import forms
from .models import Team

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'captain', 'members']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'captain': forms.Select(attrs={'class': 'form-select'}),
            'members': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
