# Generated by Django 2.0.2 on 2018-03-09 19:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20180310_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 3, 10, 0, 59, 25, 418249)),
        ),
        migrations.AlterField(
            model_name='notification',
            name='Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 3, 10, 0, 59, 25, 418249)),
        ),
        migrations.AlterField(
            model_name='panelpost',
            name='DDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 3, 10, 0, 59, 25, 418249)),
        ),
        migrations.AlterField(
            model_name='panelpost',
            name='Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 3, 10, 0, 59, 25, 418249)),
        ),
    ]
