# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-12 14:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hiking', '0012_tripreport_kind'),
    ]

    operations = [
        migrations.CreateModel(
            name='TripDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('detail', models.CharField(blank=True, max_length=1000)),
                ('url', models.CharField(blank=True, default='', max_length=1000)),
                ('kind', models.CharField(default='image', max_length=30)),
                ('hike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hiking.Hike')),
            ],
        ),
        migrations.RemoveField(
            model_name='tripreport',
            name='hike',
        ),
        migrations.DeleteModel(
            name='TripReport',
        ),
    ]
