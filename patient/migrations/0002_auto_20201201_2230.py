# Generated by Django 3.0.8 on 2020-12-01 17:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 1, 22, 30, 14, 839505)),
        ),
    ]