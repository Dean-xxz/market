import product.apis
from django.conf.urls import url

urlpatterns = [
    url(r'^product/list/$', product.apis.list_product_api, name="product_list_api"),
    url(r'^product_category/list/$', product.apis.list_product_category_api, name="product_category_list_api"),
    url(r'^product/query/$', product.apis.query_product_api, name="product_query_api"),
    url(r'^ad/list/$', product.apis.list_ad_api, name="ad_list_api"),

]
