# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-18 16:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20161218_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogimage',
            name='blogPost',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blogImages', to='blog.BlogPost'),
        ),
    ]
