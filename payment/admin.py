from django.contrib import admin
from .models import Order,Order_Goods


# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'order_goods', 'total_fee','create_time','update_time','is_payment')
    list_filter = ('is_payment','channel','is_delivery')


admin.site.register(Order, OrderAdmin)
