# Generated by Django 2.0.2 on 2018-03-19 09:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20180319_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 3, 19, 15, 3, 13, 865183)),
        ),
        migrations.AlterField(
            model_name='notification',
            name='Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 3, 19, 15, 3, 13, 865183)),
        ),
        migrations.AlterField(
            model_name='panelpost',
            name='DDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 3, 19, 15, 3, 13, 865183)),
        ),
        migrations.AlterField(
            model_name='panelpost',
            name='Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 3, 19, 15, 3, 13, 865183)),
        ),
    ]