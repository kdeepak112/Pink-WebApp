# Generated by Django 3.0.8 on 2020-12-01 17:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_auto_20201201_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 1, 22, 31, 18, 109307)),
        ),
    ]
