from django.conf.urls import url, include
from . import views, apitest

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


    # test API ,用于生成 JSON 数据做一个测试，模拟 TestMaster 返回的 branch 的信息
    url(r'^api/makebranchjson/$', apitest.makeBranchJson),
    url(r'^api/makemachinejson/$', apitest.makeMachineJson),
    url(r'^api/makecompileresult/$', apitest.makeCompileResult),

    # url(r'^api/displayjson/$', apitest.displayJson),
]
