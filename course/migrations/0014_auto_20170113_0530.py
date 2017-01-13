# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-13 05:30
from __future__ import unicode_literals

import course.models
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0013_auto_20170104_1216'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodeNinjaCache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endpoint', models.CharField(max_length=500)),
                ('lastModified', models.DateTimeField(auto_now=True)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(default=course.models.codeNinjaCacheData_default)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='codeninjacache',
            unique_together=set([('endpoint',)]),
        ),
    ]
