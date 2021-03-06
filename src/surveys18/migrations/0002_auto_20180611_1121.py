# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-11 03:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('surveys18', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='farm_related_business',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business', to='surveys18.FarmRelatedBusiness', verbose_name='Farm Related Business'),
        ),
        migrations.AlterField(
            model_name='refuse',
            name='reason',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='refuse', to='surveys18.RefuseReason', verbose_name='Refuse'),
        ),
    ]
