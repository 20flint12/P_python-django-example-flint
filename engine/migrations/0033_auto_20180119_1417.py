# Generated by Django 2.0.1 on 2018-01-19 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0032_auto_20180119_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensation',
            name='duration',
            field=models.DurationField(blank=True),
        ),
    ]
