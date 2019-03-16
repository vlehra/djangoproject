# Generated by Django 2.1.5 on 2019-02-21 17:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('address', models.TextField(blank=True, null=True)),
                ('mobile_number', models.CharField(max_length=13)),
                ('gym', models.CharField(max_length=35)),
                ('particular', models.CharField(max_length=35)),
                ('qty', models.DecimalField(decimal_places=1, max_digits=100)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=10000)),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=10000)),
                ('date_cust', models.DateTimeField(blank=True, default=datetime.datetime(2019, 2, 21, 23, 11, 50, 35146))),
            ],
        ),
    ]
