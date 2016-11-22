# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20161117_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[(b'G', b'guardian'), (b'S', b'student'), (b'I', b'instructor')], default=b'G', max_length=1),
        ),
        migrations.AlterField(
            model_name='userschoolrelation',
            name='enrollmentDate',
            field=models.DateField(auto_now_add=True),
        ),
    ]
