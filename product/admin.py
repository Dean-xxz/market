from django.contrib import admin
from .models import Category,Product

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','descp','order')


admin.site.register(Category,CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('category','title','price','pre_price','order','is_hot')
    list_filter = ('category',)


admin.site.register(Product,ProductAdmin)