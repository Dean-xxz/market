# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-06-06 01:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_remove_advertisement_is_terminal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='detail_info',
            field=models.ImageField(blank=True, null=True, upload_to='media/product/product/detail/', verbose_name='商品详情介绍图'),
        ),
    ]
