# Generated by Django 2.0.2 on 2018-05-08 17:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20180319_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 8, 22, 49, 37, 415962)),
        ),
        migrations.AlterField(
            model_name='notification',
            name='Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 8, 22, 49, 37, 415962)),
        ),
        migrations.AlterField(
            model_name='panelpost',
            name='DDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 8, 22, 49, 37, 415962)),
        ),
        migrations.AlterField(
            model_name='panelpost',
            name='Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 8, 22, 49, 37, 415962)),
        ),
    ]
