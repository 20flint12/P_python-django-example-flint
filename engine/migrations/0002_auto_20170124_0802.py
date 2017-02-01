# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-01-24 06:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moonzodiac',
            name='moon_zodiac',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='factor_mzodiac', to='engine.SummaryFactor'),
        ),
        migrations.AlterField(
            model_name='zodiaccontent',
            name='zodiac_content',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mzodiac_content', to='engine.MoonZodiac'),
        ),
    ]