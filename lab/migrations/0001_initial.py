# Generated by Django 3.0.8 on 2020-12-01 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='labsRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lab_name', models.CharField(max_length=50)),
                ('lab_contact', models.IntegerField()),
                ('lab_email', models.CharField(max_length=30)),
                ('lab_address', models.CharField(default=' ', max_length=500)),
                ('lab_password', models.CharField(default=' ', max_length=30)),
                ('lab_state', models.CharField(default='', max_length=15)),
                ('lab_district', models.CharField(default='', max_length=15)),
                ('lab_pincode', models.CharField(default='', max_length=6)),
            ],
        ),
    ]
