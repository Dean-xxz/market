from django.contrib import admin
from .models import Category,Product,Color,Image,Value,Advertisement

# Register your models here.

class AdAdmin(admin.ModelAdmin):
    list_display = ('title','order','link')

admin.site.register(Advertisement,AdAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','descp','order')


admin.site.register(Category,CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('category','title','price','pre_price','order','is_hot')
    list_filter = ('category',)


admin.site.register(Product,ProductAdmin)


class ColorAdmin(admin.ModelAdmin):
    list_display = ('product','value','order')
    list_filter = ('product',)


admin.site.register(Color,ColorAdmin)


class ImageAdmin(admin.ModelAdmin):
    list_display = ('product','image','order')
    list_filter = ('product',)


admin.site.register(Image,ImageAdmin)


class ValueAdmin(admin.ModelAdmin):
    list_display = ('product','value','order')
    list_filter = ('product',)


admin.site.register(Value,ValueAdmin)

