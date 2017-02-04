# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-01 00:00
from __future__ import unicode_literals

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20170131_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='Options: ', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]