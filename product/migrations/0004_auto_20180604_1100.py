# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-06-04 03:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_is_discount'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='value',
            options={'ordering': ['order'], 'verbose_name': '商品参数', 'verbose_name_plural': '商品参数'},
        ),
        migrations.AddField(
            model_name='product',
            name='channel',
            field=models.CharField(blank=True, choices=[('1', '联网方式1'), ('2', '联网方式2')], max_length=1, null=True, verbose_name='联网方式'),
        ),
    ]
