# Generated by Django 2.1.5 on 2019-03-13 10:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0049_auto_20190313_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 13, 16, 26, 15, 859090)),
        ),
    ]
