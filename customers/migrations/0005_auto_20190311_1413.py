# Generated by Django 2.1.5 on 2019-03-11 08:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20190311_1413'),
        ('customers', '0004_auto_20190225_2019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer_detail',
            name='name',
        ),
        migrations.RemoveField(
            model_name='customer_detail',
            name='rate',
        ),
        migrations.RemoveField(
            model_name='customer_detail',
            name='summary',
        ),
        migrations.AddField(
            model_name='customer_detail',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10000),
        ),
        migrations.AddField(
            model_name='customer_detail',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10000),
        ),
        migrations.AlterField(
            model_name='customer',
            name='date_cust',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 11, 14, 13, 17, 344713)),
        ),
        migrations.AlterField(
            model_name='customer_detail',
            name='date_cust',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 11, 14, 13, 17, 344713)),
        ),
        migrations.AlterField(
            model_name='customer_detail',
            name='mobile_number',
            field=models.CharField(max_length=12),
        ),
        migrations.RemoveField(
            model_name='customer_detail',
            name='particular',
        ),
        migrations.AddField(
            model_name='customer_detail',
            name='particular',
            field=models.ManyToManyField(blank=True, null=True, related_name='particular', to='products.Menu'),
        ),
    ]