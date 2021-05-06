from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('name/',views.create_name,name="name"),
    path('save_name/',views.save_name,name="save_name"),
    path('result/',views.result,name="result"),
]