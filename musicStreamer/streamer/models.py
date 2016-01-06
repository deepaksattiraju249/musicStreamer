from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Song(models.Model):
	name = models.CharField(max_length=100)
	url = models.CharField(max_length=200)