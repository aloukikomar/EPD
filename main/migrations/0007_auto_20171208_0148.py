# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-07 20:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20171208_0038'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=140)),
                ('Type', models.CharField(max_length=140)),
                ('To', models.CharField(default='ipec', max_length=140)),
                ('Message', models.CharField(max_length=1040)),
            ],
        ),
        migrations.AlterField(
            model_name='panelpost',
            name='Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 12, 8, 1, 48, 15, 893654)),
        ),
    ]
