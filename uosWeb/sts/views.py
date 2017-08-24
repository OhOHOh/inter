from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import RequestContext


def index(request):
    '''
    在通过密码登录的那个界面上点击“压力测试系统”, 就调用这个函数, 跳转到 .../sts/  网址
    配置一些信息, 主要是配置 TM 的地址
    :param request:
    :return:
    '''
    # return HttpResponse('sts.views.index')
    return render(request, 'sts/index.html')


def branch(request):

    return render(request, 'sts/branch.html')



def connect(request):
    if request.method == "POST":
        print('connect函数')
        name = request.POST['name']

        return render(request, 'sts/connect.html', {
            'name': name
        }, context_instance=RequestContext(request))

    return HttpResponse('views.connect')