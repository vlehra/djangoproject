# Generated by Django 2.1.5 on 2019-02-13 16:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0017_auto_20190213_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 2, 13, 21, 54, 48, 398028)),
        ),
    ]
