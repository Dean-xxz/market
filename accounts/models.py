import json
from django.db import models
from utils.basemodel.base import BaseModel
from django.core import serializers


class User_profile(BaseModel):

    """
    用户信息表：定义用户各类信息属性
    """


    phone = models.CharField(max_length = 11,verbose_name = "用户电话号码" )
    receiver = models.CharField(max_length=24,verbose_name = "收货人",null = True,blank = True )
    re_phone = models.CharField(max_length = 11,verbose_name = "收货人电话",null = True,blank = True )
    address = models.CharField(max_length = 1024,verbose_name = "收货地址",null = True,blank = True)


    class Meta:
        verbose_name = "商城用户"
        verbose_name_plural = "商城用户"
        ordering = ["-update_time",]

    def __str__(self):
        return "%s - %s" % (self.phone,self.address)


    def get_json(self):
        serials = serializers.serialize("json", [self])
        struct = json.loads(serials)
        data = struct[0]['fields']
        if 'pk' in struct[0]:
            data['id'] = struct[0]['pk']
        return data

class Info(BaseModel):
    """
    宽带信息表
    """

    user = models.ForeignKey('User_profile',verbose_name="用户",related_name="info_user")
    id_card = models.CharField(max_length=24,verbose_name="身份证号码")
    nick = models.CharField(max_length=12,verbose_name="用户姓名",null=True,blank=True)
    phone = models.CharField(max_length=11,verbose_name="预约电话")
    address = models.CharField(max_length=128,verbose_name="地址")
    date = models.CharField(max_length=128,verbose_name="预约时间")
    is_payment = models.BooleanField(verbose_name="是否付款",default=False)


    class Meta:
        verbose_name = "宽带信息"
        verbose_name_plural = "宽带信息"
        ordering = ["-update_time",]

    def __str__(self):
        return self.name


    def get_json(self):
        serials = serializers.serialize("json", [self])
        struct = json.loads(serials)
        data = struct[0]['fields']
        if 'pk' in struct[0]:
            data['id'] = struct[0]['pk']
        return data
