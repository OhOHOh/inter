"""uosWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from login import views as login_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # url(r'^cis/', include('cis.urls')),

    url(r'^$', login_views.login, name='login'),           # 登录界面
    url(r'^sts/', include('sts.urls')),                    # 压力测试系统
    url(r'^cis/', include('cis.urls')),                    # 持续集成系统



    # 所有的接口 api
    url(r'^api/v1/login/$', login_views.apiLogin, name='apilogin'),
]
