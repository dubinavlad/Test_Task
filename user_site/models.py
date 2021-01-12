from django.db import models


class Team(models.Model):
    name = models.TextField()
    tag = models.TextField()
    rating = models.IntegerField()
    wins = models.IntegerField()
    losses = models.IntegerField()
    last_match_time = models.DateField(default=None)
    logo = models.URLField()
    opendota_team_id = models.IntegerField(default=0)

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name
