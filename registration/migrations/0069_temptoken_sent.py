# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-14 03:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0068_auto_20180512_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='temptoken',
            name='sent',
            field=models.BooleanField(default=False),
        ),
    ]