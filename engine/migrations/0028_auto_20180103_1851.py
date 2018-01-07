# Generated by Django 2.0.1 on 2018-01-03 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0027_auto_20170209_0717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moondaycontent',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='moonday_imgs/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='moonzodiaccontent',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='zodiac_imgs/%Y/%m/%d/'),
        ),
    ]