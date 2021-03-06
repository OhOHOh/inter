"""mysite URL Configuration

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
from test1 import views as test1_views

app_name = 'mysiteNamespace'

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', test1_views.login),
    url(r'^test1/', include('test1.urls')),

    url(r'^api/v1/$', test1_views.connectserver),
# 作为 PING 的一个页面
    url(r'^api/v1/ping$', test1_views.ping),
]
