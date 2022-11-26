
from django.contrib import admin
from django.urls import path
from django.urls import path, re_path
from store.views import *

urlpatterns = [
    path('', index, name="index"),

]