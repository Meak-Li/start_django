"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, register_converter

from .converters import YearConverter
from .views import *

# 注册转换器
register_converter(YearConverter, 'yy')
urlpatterns = [
    path('test', test),
    path('demo', demo),
    path('user/<id>', demo_id),  # int str
    path('converter/<yy:year>', test_converter),  # 类型转换器
]
