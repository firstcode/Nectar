# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-22 03:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadApp', '0007_project_externalurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='language',
            field=models.CharField(choices=[(b'PYTHON', b'Python'), (b'MINECRAFT', b'Minecraft'), (b'3DPRINTING', b'3DPrinting'), (b'APPINVENTOR', b'AppInventor'), (b'SCRATCH', b'Scratch'), (b'JAVA', b'Java'), (b'JS', b'JavaScript'), (b'UNITY', b'Unity')], default='PYTHON', max_length=20),
        ),
    ]
