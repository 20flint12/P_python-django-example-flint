# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-01-09 08:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0003_auto_20170108_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spaceweatherdata',
            name='grabbed_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='weatherdata',
            name='grabbed_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]