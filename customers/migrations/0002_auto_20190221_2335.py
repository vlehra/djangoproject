# Generated by Django 2.1.5 on 2019-02-21 18:05

import datetime
from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date_cust',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 2, 21, 23, 35, 57, 247904)),
        ),
        migrations.AlterField(
            model_name='customer',
            name='mobile_number',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
    ]
