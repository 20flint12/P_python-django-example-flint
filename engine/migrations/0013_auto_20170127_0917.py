# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-27 07:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0012_auto_20170126_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='reminder',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='todata',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='todo',
            field=models.CharField(blank=True, default=None, max_length=250, null=True),
        ),
    ]
