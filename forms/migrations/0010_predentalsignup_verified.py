# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-03 21:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0009_predentalsignup'),
    ]

    operations = [
        migrations.AddField(
            model_name='predentalsignup',
            name='Verified',
            field=models.BooleanField(default=False),
        ),
    ]
