# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 19:56
from __future__ import unicode_literals

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0013_auto_20170320_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='due',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 3, 20, 19, 56, 13, 809124)),
        ),
    ]
