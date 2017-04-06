# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-06 01:55
from __future__ import unicode_literals

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20170403_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='Options: LegislativeCommittee ||| Conferences ||| Advocacy ||| BookClub ||| CommunityService ||| HealthAndWellness ||| Fundraising ||| Lunch ||| ', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
