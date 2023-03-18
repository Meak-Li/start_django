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
from django.contrib import admin
from django.urls import path, re_path, include

from user import urls
from user.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', login),
    path('', include(urls)),  # 增加其他的url路由地址
]
#  自定义错误页面, 这个自定义的错误页面必须在主url.py页面里面加入
#  还需要注意一点，需要将debug模式关闭，允许访问的地址更改为*
handler404 = 'user.views.page_not_found'  # 后面是对应404错误的地址


"""
几种方式添加:
可以直接写在上面：extra_url.
在对应的子应用里面直接添加url文件，使用include函数可以使用。
include(), 当很多的url都有相同的前缀时，可以使用include[]
"""
