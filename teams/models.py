from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    name = models.CharField(max_length=100)
    captain = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.TextField(help_text="Comma-separated list of team members", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
