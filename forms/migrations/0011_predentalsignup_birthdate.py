# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-03 21:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0010_predentalsignup_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='predentalsignup',
            name='BirthDate',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
