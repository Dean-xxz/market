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

    category = models.ForeignKey("Category",on_delete=models.CASCADE,related_name="product_category",verbose_name="所属商品分类",help_text="请选择该商品所属分类")
    title = models.CharField(max_length=128, verbose_name="商品标题")
    english_title = models.CharField(max_length=128,verbose_name="英文标题",null=True,blank=True)
    pre_info = models.CharField(max_length=1024,verbose_name="优惠信息",null=True,blank=True)
    descp = models.TextField(max_length=1024,verbose_name="商品简介",null=True,blank=True)
    detail_info = RichTextField(verbose_name="商品详情")
    image = models.ImageField(upload_to="media/product/product/image/",verbose_name="商品封面大图")
    detail_image = models.ImageField(upload_to="media/product/product/detail_image/",verbose_name="商品内部小图")
    price = models.DecimalField(max_digits=10 ,decimal_places =0,verbose_name="商品价格")
    pre_price = models.DecimalField(max_digits=10,decimal_places=0,verbose_name="商品优惠价格")
    count = models.IntegerField(verbose_name="商品库存",default=1)
    is_hot = models.BooleanField(verbose_name="标记为热销商品",default=False)
    order = models.PositiveSmallIntegerField(verbose_name="商品顺序",default=0,help_text="该商品在商品列表中的顺序")
    remarks = models.TextField(verbose_name="备注",null=True,blank=True)


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