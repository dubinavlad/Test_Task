from django.db import models
from django.utils.safestring import mark_safe


class Team(models.Model):
    name = models.TextField()
    tag = models.TextField()
    rating = models.IntegerField()
    wins = models.IntegerField()
    losses = models.IntegerField()
    last_match_time = models.DateField(default=None)
    logo = models.URLField()
    opendota_team_id = models.IntegerField(default=0)

    def image_tag(self):
        return mark_safe(
            '<img src="%s" width="150" height="150" />' % (self.logo)
        )

    image_tag.short_description = "Logo"

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name
