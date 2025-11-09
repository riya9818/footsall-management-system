from django import forms
from .models import Team, Player

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'age', 'position', 'contact']


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'captain', 'members']
        widgets = {
            'members': forms.CheckboxSelectMultiple(),
        }
