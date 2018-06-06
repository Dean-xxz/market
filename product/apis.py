#__author__ = "Dean"
#__email__ = "1220543004@qq.com"

"""
此处提供天易商城商品模块所需公共api
"""

from utils.view_tools import ok_json, fail_json,get_args
from utils.abstract_api import AbstractAPI
from utils.paginator import json_pagination_response, dict_pagination_response

from .models import Category,Product,Image,Color,Value,Advertisement,Mode


"""
descp:商城商品列表
input：None
output：
    image：商品封面图
    title：商品名称
    price：商品价格
    pre_info:商品优惠信息
    category：商品所属分类
    is_hot:商品是否热销
    is_discount:商品是否打折
"""
class ProductListAPI(AbstractAPI):
    def config_args(self):
        self.args = {

        }

    def access_db(self, kwarg):
        product_list = Product.objects.filter(is_active=True)
        product_list = [o.get_json() for o in product_list]
        for product in product_list:
            category_id = product['category']
            category = Category.objects.get(pk=category_id)
            category_name = category.title
            product['category_id'] = category_id
            product['category_name'] = category_name
            product.pop('is_active')
            product.pop('update_time')
            product.pop('create_time')
            product.pop('category')
            product['product_id'] = product['id']
            product.pop('id')
            product.pop('detail_info')
            product.pop('english_title')
            product.pop('descp')
            product.pop('parameter_image')
            product.pop('remarks')
        return product_list


    def format_data(self, data):
        return ok_json(data = data)


list_product_api = ProductListAPI().wrap_func()


"""
descp:产品详细信息查询接口
input:None
output:
    ……
"""

class ProductQueryAPI(AbstractAPI):
    def config_args(self):
        self.args = {
            'product_id':'r',
        }


    def access_db(self, kwarg):
        product_id = kwarg['product_id']

        product = Product.objects.get(pk = product_id)
        product = product.get_json()
        #产品基本信息
        product.pop('is_active')
        product.pop('create_time')
        product.pop('update_time')
        #产品颜色信息
        color_list = Color.objects.filter(product_id = product_id)
        color_list = [o.get_json() for o in color_list]
        for color in color_list:
            color.pop('is_active')
            color.pop('create_time')
            color.pop('update_time')
            color.pop('product')
            color['color_id'] = color['id']
            color.pop('id')
        product['color_info'] = color_list
        #产品轮播图信息
        image_list = Image.objects.filter(product_id = product_id)
        image_list = [o.get_json() for o in image_list]
        for image in image_list:
            image.pop('is_active')
            image.pop('create_time')
            image.pop('update_time')
            image['image_id'] = image['id']
            image.pop('id')
            image.pop('product')
            image.pop('remarks')
        product['image_info'] = image_list
        #产品参数信息
        value_list = Value.objects.filter(product_id = product_id)
        value_list = [o.get_json() for o in value_list]
        for value in value_list:
            value.pop('is_active')
            value.pop('create_time')
            value.pop('update_time')
            value.pop('product')
            value['value_id'] = value['id']
            value.pop('id')
        product['value_info'] = value_list
        #产品联网方式
        mode_list = Mode.objects.filter(product_id = product_id)
        mode_list = [o.get_json() for o in mode_list]
        for mode in mode_list:
            mode.pop('is_active')
            mode.pop('create_time')
            mode.pop('update_time')
            mode.pop('product')
            mode['mode_id'] = mode['id']
            mode.pop('id')
        product['mode_info'] = mode_list

        return product


    def format_data(self, data):
        return ok_json(data = data)


query_product_api = ProductQueryAPI().wrap_func()


"""
descp:首页轮播广告
input：None
output：ad_list
"""
class AdListAPI(AbstractAPI):
    def config_args(self):
        self.args = {

        }

    def access_db(self, kwarg):
        ad_list = Advertisement.objects.filter(is_active=True)
        ad_list = [o.get_json() for o in ad_list]
        for ad in ad_list:
            ad.pop('is_active')
            ad.pop('create_time')
            ad.pop('update_time')
            ad['ad_id'] = ad['id']
            ad.pop('id')
            ad.pop('remarks')
        return ad_list


    def format_data(self, data):
        return ok_json(data = data)


list_ad_api = AdListAPI().wrap_func()