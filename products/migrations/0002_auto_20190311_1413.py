# Generated by Django 2.1.5 on 2019-03-11 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=35)),
                ('description', models.TextField(blank=True, null=True)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('veg', models.BooleanField()),
                ('egg', models.BooleanField()),
                ('non_veg', models.BooleanField()),
            ],
        ),
        migrations.DeleteModel(
            name='Particular',
        ),
    ]
