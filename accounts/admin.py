from django.contrib import admin


from .models import Profile

class PersonAdmin(admin.ModelAdmin):
    list_display = ('user', 'country' , 'address' ,'joindate','is_active')
    list_filter =('user','address' ,'joindate','is_superuser','is_active')


admin.site.register(Profile ,PersonAdmin)
