from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=50)
    captain = models.CharField(max_length=50)
    members_count = models.IntegerField(default=5)

    def __str__(self):
        return self.name
