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

class PlayerAvailability(models.Model):
    STATUS_CHOICES = [
        ("available", "Available"),
        ("maybe", "Maybe"),
        ("unavailable", "Unavailable"),
    ]

    player = models.ForeignKey(Player, on_delete=models.CASCADE)
   # match = models.ForeignKey(Match, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="available")

    def __str__(self):
        return f"{self.player.name} - {self.get_status_display()}"

class MatchAttendance(models.Model):
    #match = models.ForeignKey(Match, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.player.name} - {'Present' if self.present else 'Absent'}"

class Match(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    opponent = models.CharField(max_length=100)
    match_date = models.DateTimeField()
    location = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.team.name} vs {self.opponent} on {self.match_date.strftime('%Y-%m-%d')}"