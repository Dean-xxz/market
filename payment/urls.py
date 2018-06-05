import payment.apis
from django.conf.urls import url

urlpatterns = [
    url(r'^order/create/$', payment.apis.create_order_api, name="order_create_api"),
    url(r'^order/list/$', payment.apis.list_order_api, name="order_list_api"),
]