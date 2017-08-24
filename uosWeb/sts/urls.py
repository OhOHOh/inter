from django.conf.urls import url, include
from . import views

app_name = 'sts'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^branch/$', views.branch, name='branch'),
    url(r'^connect/$', views.connect, name='connect'),
]
