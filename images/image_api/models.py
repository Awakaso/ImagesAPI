from django.db import models

# Create your models here.

class Image(models.Model):
    title = models.CharField(max_length=512)
    image_url = models.URLField(max_length=512)
    description = models.CharField(blank=True, max_length=512)

    def __str__(self):
        return self.title

