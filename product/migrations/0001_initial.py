# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-05-31 03:33
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否激活')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name='更新时间')),
                ('title', models.CharField(max_length=128, verbose_name='商品分类标题')),
                ('descp', models.CharField(blank=True, max_length=1024, null=True, verbose_name='分类描述')),
                ('order', models.PositiveSmallIntegerField(default=0, help_text='在列表中的顺序', verbose_name='分类排序')),
            ],
            options={
                'ordering': ['order'],
                'verbose_name_plural': '商品分类',
                'verbose_name': '商品分类',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否激活')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name='更新时间')),
                ('title', models.CharField(max_length=128, verbose_name='商品标题')),
                ('english_title', models.CharField(blank=True, max_length=128, null=True, verbose_name='英文标题')),
                ('pre_info', models.CharField(blank=True, max_length=1024, null=True, verbose_name='优惠信息')),
                ('descp', models.TextField(blank=True, max_length=1024, null=True, verbose_name='商品简介')),
                ('detail_info', ckeditor.fields.RichTextField(verbose_name='商品详情')),
                ('image', models.ImageField(upload_to='media/product/product/image/', verbose_name='商品封面大图')),
                ('detail_image', models.ImageField(upload_to='media/product/product/detail_image/', verbose_name='商品内部小图')),
                ('price', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='商品价格')),
                ('pre_price', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='商品优惠价格')),
                ('count', models.IntegerField(default=1, verbose_name='商品库存')),
                ('is_hot', models.BooleanField(default=False, verbose_name='标记为热销商品')),
                ('order', models.PositiveSmallIntegerField(default=0, help_text='该商品在商品列表中的顺序', verbose_name='商品顺序')),
                ('remarks', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('category', models.ForeignKey(help_text='请选择该商品所属分类', on_delete=django.db.models.deletion.CASCADE, related_name='product_category', to='product.Category', verbose_name='所属商品分类')),
            ],
            options={
                'ordering': ['order'],
                'verbose_name_plural': '商品',
                'verbose_name': '商品',
            },
        ),
    ]
