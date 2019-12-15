from django.urls import path 
from . import views
app_name= 'food'

urlpatterns = [
    path('signup/' , views.signup_view , name='sign_up'),

]
