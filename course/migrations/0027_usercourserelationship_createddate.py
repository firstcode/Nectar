# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-11 06:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0026_auto_20170217_0522'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercourserelationship',
            name='createdDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
