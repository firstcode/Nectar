# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-24 02:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0027_auto_20170320_0812'),
    ]

    operations = [
        migrations.AddField(
            model_name='referralcredit',
            name='isUsed',
            field=models.BooleanField(default=False),
        ),
    ]
