# Generated by Django 2.1.5 on 2019-03-16 18:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0019_auto_20190316_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date_cust',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 16, 23, 31, 50, 790080)),
        ),
        migrations.AlterField(
            model_name='customer_detail',
            name='date_cust',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 16, 23, 31, 50, 805702)),
        ),
    ]