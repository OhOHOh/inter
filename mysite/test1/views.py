from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import Testset, UserLogin
from django import forms
import json


# Create your views here.

# 定义表单模型
class UserLoginForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())


# 最初进入网点, 进行密码登录
def login(request):
    if request.method == 'POST':
        uf = UserLoginForm(request.POST)
        if uf.is_valid():
            # 获取表单密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # 将获取的表单的帐号与密码与数据库中的进行比对。如果成功, 那么进入 index.html 界面。
            user = UserLogin.objects.filter(username__exact=username, password__exact=password)
            if user:
                # return render(request, 'test1/index.html', context)
                return HttpResponseRedirect(reverse('test1:test1index'))
            else:
                return render(request, 'test1/login.html', {
                    'welcome': "Weclome to test1/views.login",
                    'login': "fail",
                })
    else:
        uf = UserLoginForm()
        return render(request, 'test1/login.html', {'uf': uf})


# 输入正确的密码之后, 进入网点
def index(request):
    # 从request中获取各个机器的运行状态
    context = {
        'welcome': "Welcome to test1/views.index",
    }
    return render(request, 'test1/index.html', context)


# ex: test1/connect/
# 从数据库中取得测试集的名称
def connect(request):
    testset_list = Testset.objects.order_by('setName')
    context = {
        'testset_list': testset_list,
        'welcome': "Welcome to test1/views.connect, please input",
    }
    return render(request, 'test1/connect.html', context)


# ex: test1/buildbranch/
def buildbranch(request):
    """
    从 connect.html 界面上传过来的表单数据, 将其中的 测试集名称显示在本页面( buildbranch.html )上
    :param request:
    :return:
    """
    try:
        testaddress = request.POST['testaddress233']
        testset = request.POST['testset233']
        testpatch = request.POST['testpatch233']
    except(KeyError):
        context = {'error_message': "Not find the TestMaster"}
        return fail(request, context)  # 将'失败'后返回的'失败界面'并显示'失败信息' 的行为封装成一个独立的函数 fail
        # return render(request, 'test1/fail.html', {
        #     'error_message': "Not find the TestMaster"
        # })
    else:
        context = {
            'welcome': "Welcome to test1/views.build",
            'address': testaddress,
            'set': testset[:-2],  # 删去最后2个字符 ', '
            'patch': testpatch,
        }
        print(testset)
        return render(request, 'test1/buildbranch.html', context)

    # return render(request, 'test1/buildbranch.html', context)


# ex: test1/machines/   由branch页面提交表单后跳转过来
# def machines(request):
#     # 从request中获取各个机器的运行状态, request中有 机器的测试编号, 运行时间, 运行状态, 运行距离等
#     # 如何从 request 中获取这些数据? 并封装成字典的形式?
#     try:
#         testbranch = request.POST['testaddress233']   # name 属性
#         testset = request.POST['testset233']
#         testpatch = request.POST['testpatch233']
#     except(KeyError):
#         return render(request, 'test1/connect.html', {
#             'error_message': "You didn't type the email or password.",
#         })
#     else:
#         context = {
#             'branch': testbranch,
#             'set': testset,
#             'patch': testpatch,
#             'welcome': "Welcome to test1/views.Machines",
#             'range': range(1, 16),
#         }
#         return render(request, 'test1/machines.html', context)
def machines(request):
    context = {
        'welcome': "Weclome to test1/views.machines",
        'range': range(1, 16),
    }
    return render(request, 'test1/machines.html', context)


# 持续集成系统所用的
def machinesCIS(request):
    context = {
        'welcome': "Welcome to test1/views.machinesCIS",
    }
    return render(request, 'test1/machinesCIS.html', context)


# API 接口函数
@csrf_exempt
def apiLogin(request):
    """
    通过访问 url: test1/api/login 来获取函数的执行
    :param request:
    :return:
    """
    if request.method == 'POST':
        ret = {'statusa': False, 'message': ''}
        username = request.POST.get('username')
        print(username)

        userDB = UserLogin.objects.filter(username__exact=username)
        if userDB:
            # ret['statusa'] = True
            return HttpResponse('1')
        else:
            return HttpResponse('2')

    return render(request, 'test1/login.html')

# 不是 视图函数
def fail(request, context):
    return render(request, 'test1/fail.html', context)
