from django.contrib import admin
from .models import User_profile

# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('phone','receiver','re_phone','address')
    search_fields = ('phone',)

admin.site.register(User_profile,UserProfileAdmin)
