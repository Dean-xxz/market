import json
from django.db import models
from utils.basemodel.base import BaseModel
from django.core import serializers


class User_profile(BaseModel):

    """
    用户信息表：定义用户各类信息属性
    """


    nickname = models.CharField(max_length = 24,verbose_name = "昵称",null = True,blank = True)
    phone = models.CharField(max_length = 11,verbose_name = "电话号码" )
    address = models.CharField(max_length = 1024,verbose_name = "收货地址",null = True,blank = True)


    class Meta:
        verbose_name = "订单"
        verbose_name_plural = "订单"
        ordering = ["-update_time",]

    # def __str__(self):
    #     return self.product

    def get_json(self):
        serials = serializers.serialize("json", [self])
        struct = json.loads(serials)
        data = struct[0]['fields']
        if 'pk' in struct[0]:
            data['id'] = struct[0]['pk']
        return data
