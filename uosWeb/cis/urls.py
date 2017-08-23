from django.conf.urls import url, include
from . import views

app_name = 'cis'

urlpatterns = [
    url(r'^$', views.indextest, name='index'),
]
