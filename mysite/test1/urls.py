from django.conf.urls import url, include
from . import views

app_name = 'test1'

urlpatterns = [
    url(r'^$', views.index, name='test1index'),
    url(r'^machines/$', views.machines, name='test1machines'),
    url(r'^machinesCIS/$', views.machinesCIS, name='test1machinesCIS'),
    url(r'^connect/$', views.connect, name='test1connect'),
    url(r'^buildbranch/$', views.buildbranch, name='test1build'),

    # API 接口的 url
    url(r'^api/login/$', views.apiLogin),
    url(r'^api/connecting/$', views.tryConnect),
]
