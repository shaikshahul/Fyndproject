# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-09 17:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FyndApp', '0002_auto_20180209_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='popularity',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='movies',
            name='score',
            field=models.FloatField(null=True),
        ),
    ]