# Generated by Django 2.1.5 on 2019-03-16 15:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0016_auto_20190316_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date_cust',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 16, 21, 24, 18, 757837)),
        ),
        migrations.AlterField(
            model_name='customer_detail',
            name='date_cust',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 16, 21, 24, 18, 757837)),
        ),
    ]
