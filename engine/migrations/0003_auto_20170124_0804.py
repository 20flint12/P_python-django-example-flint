# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-01-24 06:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0002_auto_20170124_0802'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moonzodiac',
            old_name='moon_zodiac',
            new_name='mzodiac',
        ),
    ]