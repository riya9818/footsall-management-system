# teams/models.py
from django.db import models

class Player(models.Model):
    POSITION_CHOICES = [
        ('GK', 'Goalkeeper'),
        ('DEF', 'Defender'),
        ('MID', 'Midfielder'),
        ('FWD', 'Forward'),
    ]

    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(null=True, blank=True)
    position = models.CharField(max_length=10, choices=POSITION_CHOICES, blank=True)
    contact = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    captain = models.ForeignKey(
        Player, on_delete=models.SET_NULL, null=True, blank=True, related_name='captained_team'
    )
    members = models.ManyToManyField(Player, related_name='teams', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
