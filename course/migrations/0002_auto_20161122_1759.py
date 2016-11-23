# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 17:59
from __future__ import unicode_literals

import course.models
from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrophyRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('trophy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Trophy')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='challenge',
            name='awardDefinition',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=course.models.awardDefinition_default),
        ),
        migrations.AddField(
            model_name='challengerecord',
            name='trophy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course.Trophy'),
        ),
        migrations.AlterUniqueTogether(
            name='trophyrecord',
            unique_together=set([('user', 'trophy')]),
        ),
    ]
