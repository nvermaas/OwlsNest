# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 11:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hiking', '0009_remove_tripreport_report_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='tripreport',
            name='title',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='tripreport',
            name='report',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='tripreport',
            name='url',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
    ]
