from django.conf.urls import url, include
from . import views

app_name = 'test1'

urlpatterns = [
    url(r'^$', views.index, name='test1index'),
    url(r'^machines/$', views.machines, name='test1machines'),
    url(r'^branch/$', views.branch, name='test1branch'),
]
