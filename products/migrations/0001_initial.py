# Generated by Django 2.1.5 on 2019-02-13 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Particular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.CharField(max_length=2)),
                ('item', models.CharField(max_length=35)),
                ('description', models.TextField(blank=True, null=True)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('veg', models.BooleanField()),
                ('egg', models.BooleanField()),
                ('non_veg', models.BooleanField()),
            ],
        ),
    ]
