# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Movies(models.Model):
    """ Movies Model Fields"""
    name = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    genre = models.CharField(max_length=1000)
    score = models.BigIntegerField()
    popularity = models.BigIntegerField()
    image = models.ImageField(upload_to=None, max_length=500, null=True)

    def __unicode__(self):
        return str(self.name)
        