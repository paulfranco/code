# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-28 19:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('high_five_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='highfive',
            old_name='giver',
            new_name='gave',
        ),
        migrations.RenameField(
            model_name='highfive',
            old_name='receiver',
            new_name='received',
        ),
    ]