# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-07 05:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0007_auto_20170108_0632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='predentalweekendsignup',
            name='ApplicantAddress',
        ),
        migrations.RemoveField(
            model_name='predentalweekendsignup',
            name='applicantContactInfo',
        ),
        migrations.RemoveField(
            model_name='predentalweekendsignup',
            name='emergencyContactInfo',
        ),
        migrations.DeleteModel(
            name='Signup',
        ),
        migrations.DeleteModel(
            name='ContactInformation',
        ),
        migrations.DeleteModel(
            name='PreDentalWeekendSignup',
        ),
        migrations.DeleteModel(
            name='UsLocation',
        ),
    ]
