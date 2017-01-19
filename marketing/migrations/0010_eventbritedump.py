# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-19 04:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0009_studentdump'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventbriteDump',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(default=None, max_length=200, null=True)),
                ('school', models.CharField(default=None, max_length=100, null=True)),
            ],
        ),
    ]
