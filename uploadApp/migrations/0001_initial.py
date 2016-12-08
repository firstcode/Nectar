# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 16:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0006_auto_20161122_1724'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('avatar_url', models.URLField(blank=True, default='http://placehold.it/350x350', verbose_name='avatar_url')),
                ('language', models.CharField(choices=[('PYTHON', 'Python'), ('MINECRAFT', 'Minecraft'), ('3DPRINTING', '3DPrinting'), ('APPINVENTOR', 'AppInventor'), ('SCRATCH', 'Scratch'), ('JAVA', 'Java'), ('JS', 'JavaScript')], default='PYTHON', max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectPackageFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploadApp.Project')),
                ('userFile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.UserFile')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectScreenshot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploadApp.Project')),
                ('userFile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.UserFile')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectSourceFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploadApp.Project')),
                ('userFile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.UserFile')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='projectsourcefile',
            unique_together=set([('project', 'userFile')]),
        ),
        migrations.AlterUniqueTogether(
            name='projectscreenshot',
            unique_together=set([('project', 'userFile')]),
        ),
        migrations.AlterUniqueTogether(
            name='projectpackagefile',
            unique_together=set([('project', 'userFile')]),
        ),
        migrations.AlterUniqueTogether(
            name='project',
            unique_together=set([('user', 'name')]),
        ),
    ]