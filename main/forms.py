# futsalapp/forms.py
from django import forms
from .models import PlayerMatchStats


class PlayerStatsForm(forms.ModelForm):
    class Meta:
        model = PlayerMatchStats
        fields = ['goals', 'assists', 'yellow_cards', 'red_cards']

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['home_team', 'away_team', 'match_date', 'match_time']



class MatchResultForm(forms.ModelForm):
    class Meta:
        model = MatchResult
        fields = ['home_score', 'away_score', 'man_of_the_match']
