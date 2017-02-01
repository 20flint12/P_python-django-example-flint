# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-01-24 06:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0004_auto_20170124_0806'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoonDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('day_choice', models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12')])),
                ('mday', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='factor_mday', to='engine.SummaryFactor')),
            ],
        ),
    ]