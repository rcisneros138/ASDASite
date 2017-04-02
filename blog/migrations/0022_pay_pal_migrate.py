# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-02 23:00
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20170206_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='videoUrlLink',
            field=models.CharField(blank=True, max_length=2000, null=True, validators=[django.core.validators.URLValidator()]),
        ),
    ]
