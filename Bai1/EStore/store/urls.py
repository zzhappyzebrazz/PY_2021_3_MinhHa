
from django.contrib import admin
from django.urls import path
from django.urls import path, re_path
from store.views import *

urlpatterns = [
    path('', index, name="index"),
    path('cart/', cart, name="cart"),
    path('checkout/', checkout, name="checkout"),
    path('contact/', contact, name="contact"),
    path('login/', login, name="login"),
    path('my_account/', my_account, name="my_account"),
    path('product_detail/', product_detail, name="my_account"),
    path('product_list/', product_list, name="my_account"),
    path('wishlist/', wishlist, name="wishlist"),
]