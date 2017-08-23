from django.conf.urls import url, include
from . import views

app_name = 'sts'

urlpatterns = [
    url(r'^$', views.indextest, name='index'),
]
