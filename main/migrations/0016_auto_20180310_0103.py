# Generated by Django 2.0.2 on 2018-03-09 19:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20180310_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 3, 10, 1, 3, 39, 43399)),
        ),
        migrations.AlterField(
            model_name='notification',
            name='Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 3, 10, 1, 3, 39, 41899)),
        ),
        migrations.AlterField(
            model_name='panelpost',
            name='DDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 3, 10, 1, 3, 39, 25768)),
        ),
        migrations.AlterField(
            model_name='panelpost',
            name='Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 3, 10, 1, 3, 39, 25768)),
        ),
    ]
