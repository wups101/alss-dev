# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-24 06:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys18', '0004_auto_20180523_1519'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='numberworkers',
            name='value',
        ),
        migrations.AddField(
            model_name='numberworkers',
            name='count',
            field=models.IntegerField(blank=True, null=True, verbose_name='Count'),
        ),
    ]
