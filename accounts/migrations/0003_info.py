# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-06-12 01:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180604_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否激活')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name='更新时间')),
                ('id_card', models.CharField(max_length=24, verbose_name='身份证号码')),
                ('name', models.CharField(max_length=12, verbose_name='用户姓名')),
                ('phone', models.CharField(max_length=11, verbose_name='预约电话')),
                ('address', models.CharField(max_length=128, verbose_name='地址')),
                ('date', models.CharField(max_length=128, verbose_name='预约时间')),
                ('is_payment', models.BooleanField(default=False, verbose_name='是否付款')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='info_user', to='accounts.User_profile', verbose_name='用户')),
            ],
            options={
                'ordering': ['-update_time'],
                'verbose_name_plural': '宽带信息',
                'verbose_name': '宽带信息',
            },
        ),
    ]