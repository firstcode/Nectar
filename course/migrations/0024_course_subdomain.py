# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-09 09:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0023_auto_20170209_0833'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='subdomain',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
    ]