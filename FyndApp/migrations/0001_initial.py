# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-07 17:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('director', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=1000)),
                ('score', models.BigIntegerField()),
                ('popularity', models.BigIntegerField()),
                ('image', models.ImageField(max_length=500, null=True, upload_to=None)),
            ],
        ),
    ]
