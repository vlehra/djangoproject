# Generated by Django 2.1.5 on 2019-03-16 17:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0059_auto_20190316_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 16, 23, 4, 23, 246618)),
        ),
    ]
