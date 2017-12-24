# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-28 06:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('alias', models.CharField(default='None', max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('bday', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('password', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
