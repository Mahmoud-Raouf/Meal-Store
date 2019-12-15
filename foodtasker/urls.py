from django.contrib import admin
from django.urls import path , include
from food import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/' , include('django.contrib.auth.urls')),
    path('accounts/' , include('accounts.urls',namespace='signup')),
    path('restaurant/' , include('food.urls' , namespace='food'))

]
