# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-16 13:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MiniURL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longUrl', models.URLField(unique=True, verbose_name='URL à réduire')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('pseudo', models.CharField(blank=True, max_length=10)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name="Date d'enregistrement")),
                ('access', models.IntegerField(default=0, verbose_name="Nombre d'accès à l'URL")),
            ],
        ),
    ]