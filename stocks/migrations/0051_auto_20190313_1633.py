# Generated by Django 2.1.5 on 2019-03-13 11:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0050_auto_20190313_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 13, 16, 33, 28, 985699)),
        ),
    ]
