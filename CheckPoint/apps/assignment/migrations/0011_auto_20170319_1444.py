# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-19 14:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0010_auto_20170319_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='due',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 3, 19, 14, 44, 48, 58373)),
        ),
    ]
