
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('new', views.new, name="new"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('delete/<int:id>', views.delete, name="delete"),
]
