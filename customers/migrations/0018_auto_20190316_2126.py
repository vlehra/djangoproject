# Generated by Django 2.1.5 on 2019-03-16 15:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0017_auto_20190316_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date_cust',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 16, 21, 26, 9, 958321)),
        ),
        migrations.AlterField(
            model_name='customer_detail',
            name='date_cust',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 16, 21, 26, 9, 966361)),
        ),
    ]