from django.contrib import admin
from django.urls import path
from django.urls import path, re_path
from store.views import *

app_name = 'store'

urlpatterns = [
    # path('', index, name="index"),
    path('cart/', cart, name="cart"),
    path('checkout/', checkout, name="checkout"),
    path('contact/', contact, name="contact"),
    path('product_detail/<int:pk>/', product_detail, name="product_detail"),
    path('subcategory/<int:pk>/', subcategory, name="subcategory"),
    # path('wishlist/', wishlist, name="wishlist"),
    path('', index_2, name="index_2"),
    path('auth_user', demo_auth_user, name="auth_user"),
]