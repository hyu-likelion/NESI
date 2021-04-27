from django.contrib import admin
from django.urls import path
from survey import views

urlpatterns = [
    path('', views.home, name="home"),
    path('detail/<int:id>', views.detail, name="detail"),
    path('results/<int:id>', views.results, name="results"),
]
