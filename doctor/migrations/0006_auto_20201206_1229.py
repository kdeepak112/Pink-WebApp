# Generated by Django 3.0.8 on 2020-12-06 06:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0005_auto_20201206_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 6, 12, 29, 46, 781638)),
        ),
    ]
