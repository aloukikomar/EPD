# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-07 20:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20171208_0220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 12, 8, 2, 21, 1, 727786)),
        ),
        migrations.AlterField(
            model_name='panelpost',
            name='Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 12, 8, 2, 21, 1, 727786)),
        ),
    ]
