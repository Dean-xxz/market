"""
此处定义商品模块模型：
    商品分类表
    商品表
    一对多关系
"""

import json
from django.db import models
from utils.basemodel.base import BaseModel
from django.core import serializers
from ckeditor.fields import RichTextField
from redactor.fields import RedactorField


# Create your models here.
class Category(BaseModel):

    """
    商品分类表：定义商品分类，eg：水果；奶茶；家具……
    """
    title = models.CharField(max_length=128, verbose_name="商品分类标题")
    descp = models.CharField(max_length=1024,verbose_name="分类描述",null=True,blank=True)
    order = models.PositiveSmallIntegerField(verbose_name="分类排序",default=0,help_text="在列表中的顺序")


    class Meta:
        verbose_name = "商品分类"
        verbose_name_plural = "商品分类"
        ordering = ['order',]

    def __str__(self):
        return self.title

    def get_json(self):
        serials = serializers.serialize("json", [self])
        struct = json.loads(serials)
        data = struct[0]['fields']
        if 'pk' in struct[0]:
            data['id'] = struct[0]['pk']
        return data



class Product(BaseModel):

    """
    商品表：定义商品详细属性
    """
    CHOICES = (
            ('1',("联网方式1")),
            ('2',("联网方式2")),
        )

    category = models.ForeignKey("Category",on_delete=models.CASCADE,related_name="product_category",verbose_name="所属商品分类",help_text="请选择该商品所属分类")
    title = models.CharField(max_length=128, verbose_name="商品标题")
    english_title = models.CharField(max_length=128,verbose_name="英文标题",null=True,blank=True)
    pre_info = models.CharField(max_length=1024,verbose_name="优惠信息",null=True,blank=True)
    descp = models.TextField(max_length=1024,verbose_name="商品简介",null=True,blank=True)
    detail_info = models.ImageField(upload_to="media/product/product/detail/",verbose_name="商品详情介绍图",null=True,blank=True)
    image = models.ImageField(upload_to="media/product/product/image/",verbose_name="商品封面大图")
    price = models.DecimalField(max_digits=10 ,decimal_places =0,verbose_name="商品价格")
    parameter_image = models.ImageField(upload_to="media/product/product/parameter_image",verbose_name="商品参数图片",null=True,blank=True)
    pre_price = models.DecimalField(max_digits=10,decimal_places=0,verbose_name="商品优惠价格")
    count = models.IntegerField(verbose_name="商品库存",default=1)
    is_hot = models.BooleanField(verbose_name="标记为热销商品",default=False)
    is_discount = models.BooleanField(verbose_name="标记为打折商品",default=False)
    order = models.PositiveSmallIntegerField(verbose_name="商品顺序",default=0,help_text="该商品在商品列表中的顺序")
    remarks = models.TextField(verbose_name="备注",null=True,blank=True)
    channel = models.CharField(max_length = 1,verbose_name = "联网方式",null = True,blank = True,choices = CHOICES)


    class Meta:
        verbose_name = "商品"
        verbose_name_plural = "商品"
        ordering = ['order',]

    def __str__(self):
        return self.title

    def get_json(self):
        serials = serializers.serialize("json", [self])
        struct = json.loads(serials)
        data = struct[0]['fields']
        if 'pk' in struct[0]:
            data['id'] = struct[0]['pk']
        return data



class Image(BaseModel):


    """
    商品图片表：商品详情页面的轮播图片
    """

    product = models.ForeignKey('Product',related_name="image_product",verbose_name='所属商品')
    image = models.ImageField(upload_to="media/product/image",verbose_name="商品轮播图")
    order = models.PositiveSmallIntegerField(verbose_name="图片顺序",default=0,help_text="该图片在图片列表中的顺序")
    remarks = models.CharField(max_length=1024,verbose_name="备注",null=True,blank=True)


    class Meta:
        verbose_name = "轮播图片"
        verbose_name_plural = "轮播图片"
        ordering = ['order',]


    def get_json(self):
        serials = serializers.serialize("json", [self])
        struct = json.loads(serials)
        data = struct[0]['fields']
        if 'pk' in struct[0]:
            data['id'] = struct[0]['pk']
        return data



class Color(BaseModel):

    """
    商品颜色表：标明商品的颜色属性
    """
    product = models.ForeignKey('Product',related_name="color_product",verbose_name='所属商品')
    title = models.CharField(max_length=12,verbose_name='颜色标题',null=True,blank=True)
    value = models.CharField(max_length=1024,verbose_name="色值",null=True,blank=True)
    image = models.ImageField(upload_to="media/product/color",verbose_name="颜色图片",null=True,blank=True)
    order = models.PositiveSmallIntegerField(verbose_name="颜色顺序",default=0,help_text="该颜色在颜色列表中的顺序")


    class Meta:
        verbose_name = "商品颜色"
        verbose_name_plural = "商品颜色"
        ordering = ['order',]



    def __str__(self):
        return self.value

    def get_json(self):
        serials = serializers.serialize("json", [self])
        struct = json.loads(serials)
        data = struct[0]['fields']
        if 'pk' in struct[0]:
            data['id'] = struct[0]['pk']
        return data




class Value(BaseModel):

    """
    商品重要参数
    """
    product = models.ForeignKey('Product',related_name="value_product",verbose_name='所属商品')
    value = models.CharField(max_length=128,verbose_name="参数内容")
    order = models.PositiveSmallIntegerField(verbose_name="参数顺序",default=0,help_text="该参数在参数列表中的顺序")


    class Meta:
        verbose_name = "商品参数"
        verbose_name_plural = "商品参数"
        ordering = ['order',]



    def __str__(self):
        return self.value

    def get_json(self):
        serials = serializers.serialize("json", [self])
        struct = json.loads(serials)
        data = struct[0]['fields']
        if 'pk' in struct[0]:
            data['id'] = struct[0]['pk']
        return data



class Advertisement(BaseModel):

    """
    首页轮播广告
    """
    title = models.CharField(max_length=128,verbose_name="广告标题",null=True,blank=True)
    link = models.CharField(max_length=128,verbose_name="广告链接",null=True,blank=True)
    image = models.ImageField(upload_to="media/ad/img/",verbose_name="广告图片",null=True,blank=True)
    video = models.FileField(upload_to="media/ad/video/",verbose_name="广告视频",null=True,blank=True)
    order = models.PositiveSmallIntegerField(verbose_name = "顺序",default = 1,help_text = "该广告在广告列表中的顺序")
    remarks = models.TextField(verbose_name="备注、描述",null=True,blank=True,help_text="请输入备注、描述等")


    class Meta:
        verbose_name = "轮播广告"
        verbose_name_plural = "轮播广告"
        ordering = ["order",]

    def __str__(self):
        return self.title

    def get_json(self):
        serials = serializers.serialize("json", [self])
        struct = json.loads(serials)
        data = struct[0]['fields']
        if 'pk' in struct[0]:
            data['id'] = struct[0]['pk']
        return data
