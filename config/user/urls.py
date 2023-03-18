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
from django.urls import path, register_converter, re_path

from .converters import YearConverter
from .views import *

# 注册转换器
register_converter(YearConverter, 'yy')
urlpatterns = [
    path('test', test),
    path('demo', demo),
    path('user/<id>', demo_id),  # int str
    path('converter/<yy:year>', test_converter),  # 类型转换器
    # re_path(r'^re/(?P<year>[0-9]{4})', test_re_path), # 正则，(P<name>pattern)  # 先匹配到后不会匹配到下面的url
    re_path(r'^re/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})', test_month_re_path),  # 正则，(P<name>pattern)
    re_path(r'^re/(?:year-(?P<year>[0-9]{4}))', test_repath_standard),  # 正则标准的，嵌入一个字符串
    path('blog', get_info),  # 默认值, 是使用的两个url地址，没有输入参数的时候，匹配此url， 有参数的时候走的是下面的url
    path('blog/<int:page>', get_info),  # 默认值
    path('other_arg', other_arg, {'info': '2023年'}),  # 额外参数, 写在后面
    path('index', index, name='ind'),
    path('index/<int:page>', index_page, name='in_page'),
    path('reverse', redirect_to_index),
]
