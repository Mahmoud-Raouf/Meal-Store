from django.shortcuts import render ,get_object_or_404 ,redirect
from django.contrib.auth.models import User
from .models import Restaurant
# from .forms import UserForms , RestaurantForms
from django.contrib.auth import login , authenticate

def product_list(request):

    product_list = Restaurant.objects.all()
    context={
        'product_list' : product_list
    }
    return render(request , 'product_list.html' ,context)

def product_detial(request , slug):

    product_detial = get_object_or_404(Restaurant , slug=slug)
    context = {
        'product_detial' : product_detial
    }
    return render(request , 'product_detial.html' ,context)

