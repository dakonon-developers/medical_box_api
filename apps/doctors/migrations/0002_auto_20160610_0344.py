# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-10 03:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
