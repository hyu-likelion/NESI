from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name="main"),
    path('calculator/', views.calculator, name="calculator")
# 메인페이지 url
# calculator 페이지 url
]