#__author__ = "Dean"
#__email__ = "1220543004@qq.com"

"""
此处提供天易商城 订单支付模块所需公共api
"""
import json
from utils.view_tools import ok_json, fail_json,get_args
from utils.abstract_api import AbstractAPI
from django.views.generic import View
from django.http import HttpResponse
from .models import Order,Order_Goods
from accounts.models import User_profile

"""
descp：创建订单接口
input：
        total_fee:订单价格
        product_id:商品id
        value_id:商品参数id
        color_id:商品颜色id
        user_id:用户id
        channel:支付方式 W：微信，Z：支付宝
"""
class OrderCreateAPI(AbstractAPI):
    def config_args(self):
        self.args = {
            'user_id':'r',
            'product_id':'r',
            'channel':'r',
            'value_id':'r',
            'color_id':'r',
            'total_fee':'r',
        }

    def access_db(self, kwarg):
        user_id = kwarg['user_id']
        product_id = kwarg['product_id']
        channel = kwarg['channel']
        value_id = kwarg['value_id']
        color_id = kwarg['color_id']
        total_fee = kwarg['total_fee']

        order_goods = Order_Goods(product_id = product_id,value_id = value_id,color_id = color_id)
        order_goods.save()
        if order_goods:
            order_goods_id = order_goods.id
            order = Order(order_goods_id = order_goods_id,channel = channel,user_id = user_id,total_fee = total_fee)
            order.save()
            data = order.get_json()
            # if channel == 'W':
            #     #微信支付
            # if channel == 'Z':
            #     #支付宝支付
            return data

    def format_data(self, data):
        return ok_json(data = data)

create_order_api = OrderCreateAPI().wrap_func()

"""
descp:订单列表查询
input：user_id 用户id
output：
    订单列表信息
"""
class OrderListAPI(AbstractAPI):
    def config_args(self):
        self.args = {
            'user_id':'r',
        }

    def access_db(self, kwarg):
        user_id = kwarg['user_id']

        order_list = Order.objects.filter(user_id = user_id)
        order_list = [o.get_json() for o in order_list]
        for order in order_list:
            order.pop('is_active')
            order['order_id'] = order['id']
            order.pop('id')
            user_id = order['user']
            user = User_profile.objects.get(pk=user_id)
            user = user.get_json()
            user.pop('is_active')
            user.pop('update_time')
            user.pop('create_time')
            user['user_id'] = user['id']
            user.pop('id')
            order['user_info'] = user
            goods_id = order['order_goods']
            product = Order_Goods.objects.get(pk=goods_id)
            product_title = product.product.title
            product_color = product.color.title
            product_value = product.value.value
            product_mode = product.mode.title
            product_info = {
                'product_title':product_title,
                'product_color':product_color,
                'product_value':product_value,
                'product_mode':product_mode
            }
            order['product_info'] = product_info
            order.pop('user')



        return order_list


    def format_data(self, data):
        return ok_json(data = data)

list_order_api = OrderListAPI().wrap_func()


