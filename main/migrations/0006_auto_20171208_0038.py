# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-07 19:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20171208_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='panelpost',
            name='Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 12, 8, 0, 38, 21, 208087)),
        ),
        migrations.AlterField(
            model_name='panelpost',
            name='Type',
            field=models.CharField(choices=[('placement', 'placement'), ('congractulations', 'congratulations'), ('list of students', 'list of students'), ('notice', 'notice')], default='notice', max_length=200),
        ),
    ]
