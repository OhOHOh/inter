"""connectServer URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from api import views as api_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^api/v1/hello/$', api_views.hello),
    # test API ,用于生成 JSON 数据做一个测试，模拟 TestMaster 返回的 branch 的信息
    url(r'^api/v1/branches/$', api_views.makeBranchJson),               # api/v1/branches
    url(r'^api/v1/machines/$', api_views.makeMachineJson),              # api/v1/machines
    url(r'^api/v1/makecompileresult/$', api_views.makeCompileResult),
    url(r'^api/v1/testcases/$', api_views.makeCase),                    # api/v1/testcases
]
