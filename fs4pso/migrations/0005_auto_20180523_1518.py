# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-23 06:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fs4pso', '0004_subject_created_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='subject',
            new_name='subject_name',
        ),
    ]
