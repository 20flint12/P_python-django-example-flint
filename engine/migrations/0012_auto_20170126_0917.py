# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-01-26 07:17
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0011_place_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='dst',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='place',
            name='latitude',
            field=models.FloatField(blank=True, default=None, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(180.0)]),
        ),
        migrations.AddField(
            model_name='place',
            name='longitude',
            field=models.FloatField(blank=True, default=None, null=True, validators=[django.core.validators.MinValueValidator(-90.0), django.core.validators.MaxValueValidator(90.0)]),
        ),
        migrations.AddField(
            model_name='place',
            name='timezone',
            field=models.CharField(blank=True, default=None, max_length=250, null=True),
        ),
    ]
