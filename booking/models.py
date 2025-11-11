# bookings/models.py
from django.db import models
from teams.models import Team

class Ground(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=150)
    price_per_hour = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bookings')
    opponent_team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='opponent_matches')
    ground = models.ForeignKey(Ground, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.team.name} vs {self.opponent_team} @ {self.ground.name}"
