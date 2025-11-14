from django.db import models

# Create your models here.
class Match(models.Model):
    home_team = models.ForeignKey(Team, related_name="home_matches", on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, related_name="away_matches", on_delete=models.CASCADE)
    match_date = models.DateField()
    match_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)