from django.contrib import admin
from django.urls import path
from django.urls import path, re_path
from customer.views import *

app_name = 'customer'

urlpatterns = [
    path('dang-nhap', login, name="login"),
    path('my_account', my_account, name="my_account"),
    path('logout', log_out, name="logout"),
]