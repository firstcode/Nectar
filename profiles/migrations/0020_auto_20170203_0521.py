# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-03 05:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0019_ledger_signby'),
    ]

    operations = [
        migrations.AddField(
            model_name='ledger',
            name='remarks',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='ledger',
            name='source',
            field=models.CharField(choices=[(b'CC', b'credit card'), (b'CASH', b'cash'), (b'CHECK', b'check'), (b'OTHER', b'other')], default=b'OTHER', max_length=10),
        ),
    ]