from django.urls import path,include
from . import views

urlpatterns = [
    path('main/',views.main,name="main"),
    path('calculator/',views.calculator,name="calculator"),

]