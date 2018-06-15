from django.contrib import admin
from .models import User_profile,Info

# Register your models here.

class InfoAdmin(admin.ModelAdmin):
    list_display = ('user_id','nick','phone','address','id_card','is_payment')
    list_filter = ('is_payment',)

admin.site.register(Info,InfoAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('phone','receiver','re_phone','address')
    search_fields = ('phone',)

admin.site.register(User_profile,UserProfileAdmin)
