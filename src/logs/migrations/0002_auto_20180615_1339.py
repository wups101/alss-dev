# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-15 05:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewlog',
            name='update_datetime',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Updated'),
        ),
        migrations.AlterField(
            model_name='reviewlog',
            name='current_errors',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Current Error Count'),
        ),
        migrations.AlterField(
            model_name='reviewlog',
            name='initial_errors',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Initialed Error Count'),
        ),
        migrations.AlterField(
            model_name='reviewlog',
            name='skip_errors',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Skipped Error Count'),
        ),
    ]
