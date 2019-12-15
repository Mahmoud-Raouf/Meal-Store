from django.urls import path 

from . import views

app_name= 'food'

urlpatterns = [
    path('' , views.product_list),
    path('<slug:slug>' , views.product_detial , name='product_detial'),
    # path('signup/' , views.sign_up , name='sign_up'),

]
