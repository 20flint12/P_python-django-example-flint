# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0002_recnews'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weather_datetime', models.DateTimeField()),
                ('check_time', models.CharField(max_length=5)),
                ('temperature_air', models.FloatField()),
                ('temperature_com', models.IntegerField()),
                ('temperature_dew', models.IntegerField()),
                ('temperature_hum', models.IntegerField()),
                ('pressure_sea', models.IntegerField()),
                ('pressure_stn', models.IntegerField()),
            ],
        ),
    ]
