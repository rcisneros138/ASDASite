# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-08 06:34
from __future__ import unicode_literals

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20170108_0632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taggedblog',
            name='content_object',
        ),
        migrations.RemoveField(
            model_name='taggedblog',
            name='tag',
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.DeleteModel(
            name='TaggedBlog',
        ),
    ]