# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-12 21:49
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20170108_0634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
