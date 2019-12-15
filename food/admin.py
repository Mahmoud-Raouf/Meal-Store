from django.contrib import admin

from .models import Restaurant


class AdminField(admin.ModelAdmin):
    list_display = ['name' , 'phone','address','slug']
    list_filter  = ['address', 'phone', 'name']

    
admin.site.register(Restaurant , AdminField)
