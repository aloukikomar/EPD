# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-07 20:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20171208_0148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='Type',
        ),
        migrations.AddField(
            model_name='notification',
            name='Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 12, 8, 2, 20, 55, 455841)),
        ),
        migrations.AddField(
            model_name='notification',
            name='Roll',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='panelpost',
            name='Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 12, 8, 2, 20, 55, 455841)),
        ),
    ]
