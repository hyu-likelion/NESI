from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.welcome,name="welcome"),
    path('home/',views.home,name="home"),
    path('home/wc',views.result,name="wordcount"),
    path('namecard/',views.namecard,name='namecard'),

]