# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-06-13 06:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20180613_0649'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info',
            old_name='name',
            new_name='nick',
        ),
    ]
