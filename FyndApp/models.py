# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Movies(models.Model):
    """ Movies Model Fields"""
    name = models.CharField(max_length=200, null=True)
    director = models.CharField(max_length=200, null=True)
    genre = models.CharField(max_length=1000, null=True)
    score = models.FloatField(null=True)
    popularity = models.FloatField(null=True)
    image = models.ImageField(upload_to=None, default='no-img.jpg', null=True)
    release_date = models.DateField(null=True)
    country = models.CharField(max_length=200, null=True)
    language = models.CharField(max_length=200, null=True)
    storyline = models.TextField(null=True)
    cast = models.TextField(null=True)
    youtube = models.URLField(null=True)

    def __unicode__(self):
        return str(self.name)
        