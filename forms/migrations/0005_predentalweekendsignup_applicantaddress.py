# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-27 23:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0004_auto_20161119_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='predentalweekendsignup',
            name='ApplicantAddress',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ApplicantAddress', to='forms.UsLocation'),
        ),
    ]
