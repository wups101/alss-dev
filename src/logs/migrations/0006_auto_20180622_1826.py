# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-22 10:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0005_auto_20180622_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewlog',
            name='update_datetime',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Updated'),
        ),
    ]
