# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-05-31 03:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否激活')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name='更新时间')),
                ('nickname', models.CharField(blank=True, max_length=24, null=True, verbose_name='昵称')),
                ('phone', models.CharField(max_length=11, verbose_name='电话号码')),
                ('address', models.CharField(blank=True, max_length=1024, null=True, verbose_name='收货地址')),
            ],
            options={
                'verbose_name_plural': '订单',
                'ordering': ['-update_time'],
                'verbose_name': '订单',
            },
        ),
    ]
