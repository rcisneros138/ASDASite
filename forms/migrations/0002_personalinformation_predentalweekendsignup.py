# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-16 22:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(blank=True, max_length=140, null=True, verbose_name='First Name')),
                ('lastName', models.CharField(blank=True, max_length=140, null=True, verbose_name='Last Name')),
                ('ContactNumber', models.CharField(blank=True, max_length=140, null=True, verbose_name='Contact Number')),
            ],
        ),
        migrations.CreateModel(
            name='PreDentalWeekendSignup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(blank=True, max_length=140, null=True, verbose_name='First Name')),
                ('lastName', models.CharField(blank=True, max_length=140, null=True, verbose_name='Last Name')),
                ('mailingAddress', models.TextField(verbose_name='Address')),
                ('school', models.CharField(blank=True, max_length=140, null=True, verbose_name='school')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('emergencyContactName', models.CharField(blank=True, max_length=140, null=True, verbose_name='Contact Name')),
                ('emergencyContactPhone', models.CharField(blank=True, max_length=140, null=True, verbose_name='Contact Phone')),
                ('needsHotelRoom', models.BooleanField(default=False, verbose_name='Needs Hotel')),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
