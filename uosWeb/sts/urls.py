from django.conf.urls import url, include
from . import views

app_name = 'sts'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^branch/$', views.branch, name='branch'),
    url(r'^connect/$', views.connect2, name='connect'),
    url(r'^machine/$', views.machine2, name='machine'),

# 网页访问的是本项目内部的以下 API：(浏览器不会在地址栏中输入下列 url, 这些 api 只会在某些网页中的按钮点击事件中被访问, 它们的 url 没有意义)
    url(r'^api/tryconnect/$', views.tryConnect, name='tryconnect'),
    url(r'^api/ping/$', views.tryPing, name='tryping'),
]
