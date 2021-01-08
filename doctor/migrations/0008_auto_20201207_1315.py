# Generated by Django 3.0.8 on 2020-12-07 07:45

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0014_auto_20201207_1315'),
        ('doctor', '0007_auto_20201207_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 7, 13, 15, 55, 91653)),
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report', models.FileField(null=True, upload_to='')),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2020, 12, 7, 13, 15, 55, 92651))),
                ('from_doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='doctor.DoctorProfile')),
                ('to_patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='patient.patient')),
            ],
        ),
    ]