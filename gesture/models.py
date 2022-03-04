from django.db import models
from django.conf import settings

from pathlib import Path

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Reference(models.Model):
    image = models.ImageField(upload_to='', null=True)
    when_drawn = models.DateTimeField('Time when this reference was drawn.',null=True,blank=True)
    tags = models.ManyToManyField(Tag,blank=True)

    def __str__(self):
        return self.image.name
