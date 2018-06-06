
"""
此模块定义商城订单模型
"""

# Create your models here.
import json
from django.db import models
from utils.basemodel.base import BaseModel
from django.core import serializers
from product.models import Product,Color,Value,Image,Mode
from accounts.models import User_profile


class Order(BaseModel):

    """
    支付系统订单表，外键关联产品表Product
    """
    CHANNEL_CHOICES = (
            ('Z',("支付宝支付")),
            ('W',("微信支付")),
        )

    user = models.ForeignKey('accounts.User_profile',on_delete=models.CASCADE,verbose_name = "用户",related_name = "order_user",null=True,blank=True)
    order_goods = models.ForeignKey("Order_Goods",on_delete=models.CASCADE,verbose_name = "订单商品",related_name = "product_goods",null=True,blank=True)
    total_fee = models.DecimalField(max_digits = 10,decimal_places = 2,verbose_name="总价")
    channel = models.CharField(max_length = 1,verbose_name = "支付渠道",null = True,blank = True,choices = CHANNEL_CHOICES)
    is_payment = models.BooleanField(verbose_name="是否付款",default=False)
    is_delivery =models.BooleanField(verbose_name="是否发货",default=False)
    is_refound = models.BooleanField(verbose_name="是否退款",default=False)
    remarks = models.CharField(max_length=1024,verbose_name="备注",null=True,blank=True)


    class Meta:
        verbose_name = "订单"
        verbose_name_plural = "订单"
        ordering = ["-update_time",]


    def get_json(self):
        serials = serializers.serialize("json", [self])
        struct = json.loads(serials)
        data = struct[0]['fields']
        if 'pk' in struct[0]:
            data['id'] = struct[0]['pk']
        return data


class Order_Goods(BaseModel):
    """
    订单商品表；标明该订单的商品及各种属性信息
    """
    product = models.ForeignKey("product.Product",on_delete=models.CASCADE,verbose_name = "商品",related_name = "goods_product",null=True,blank=True)
    color = models.ForeignKey("product.Color",verbose_name="商品颜色",related_name = "goods_color",null=True,blank=True)
    value = models.ForeignKey("product.Value",verbose_name="商品规格",related_name = "goods_value",null=True,blank=True)
    mode = models.ForeignKey("product.Mode",verbose_name="商品联网方式",related_name = "goods_mode",null=True,blank=True)


    class Meta:
        verbose_name = "订单商品"
        verbose_name_plural = "订单商品"
        ordering = ["-update_time",]

    def __str__(self):
        return "%s - %s - %s - %s"%(self.product.title,self.mode.title,self.color.title,self.value.value)


    def get_json(self):
        serials = serializers.serialize("json", [self])
        struct = json.loads(serials)
        data = struct[0]['fields']
        if 'pk' in struct[0]:
            data['id'] = struct[0]['pk']
        return data
