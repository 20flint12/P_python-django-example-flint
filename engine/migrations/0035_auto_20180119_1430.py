# Generated by Django 2.0.1 on 2018-01-19 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0034_auto_20180119_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensation',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='sensation',
            name='user_profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_sensations', to='astrouser.UserProfile'),
        ),
    ]
