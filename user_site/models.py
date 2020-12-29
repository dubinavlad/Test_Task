from django.db import models
from PIL import Image
from resizeimage import resizeimage
from io import BytesIO
from django.core.files.base import ContentFile

class Team(models.Model):
    name = models.CharField(max_length=255)
    tag=models.CharField(max_length=50)
    rating = models.IntegerField()
    wins=models.IntegerField()
    losses=models.IntegerField()
    last_match_time = models.DateField(default=None)
    logo = models.URLField()
    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name

