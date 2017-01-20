# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-01-08 19:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpaceWeatherData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grabbed_at', models.DateTimeField(default=datetime.datetime(2017, 1, 8, 19, 54, 11, 465948, tzinfo=utc))),
                ('activity_level', models.CharField(max_length=5)),
                ('p_00_24_hr', models.IntegerField()),
                ('p_24_48_hr', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='weatherdata',
            old_name='check_time',
            new_name='check_timestamp',
        ),
        migrations.RemoveField(
            model_name='weatherdata',
            name='weather_datetime',
        ),
        migrations.AddField(
            model_name='weatherdata',
            name='grabbed_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 8, 19, 54, 11, 465309, tzinfo=utc)),
        ),
    ]