"""Mylinebot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MylinebotApp import views #MylinebotApp改成自己綠色的資料夾

urlpatterns = [
    path('admin/', admin.site.urls),
    path('callback', views.callback),
    path('^index',views.index),#當進入http://domain/index網址時，觸發index函數
]

# from django.urls import include, re_path
# from django.contrib import admin

# urlpatterns = [
#     re_path(r'^admin/', admin.site.urls),
#     re_path(r'^MylinebotApp/', include('MylinebotApp.urls')), #MylinebotApp改成自己綠色的資料夾名稱
# ]