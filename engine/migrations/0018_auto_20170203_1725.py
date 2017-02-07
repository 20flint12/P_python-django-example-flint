# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 15:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0017_auto_20170203_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moonday',
            name='mday',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_mday', to='engine.SummaryFactor'),
        ),
        migrations.AlterField(
            model_name='moondaycontent',
            name='mdcontent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_mdcontent', to='engine.MoonDay'),
        ),
        migrations.AlterField(
            model_name='place',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_profile', to='astrouser.UserProfile'),
        ),
    ]