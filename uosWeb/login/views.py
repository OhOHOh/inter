from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django import forms

# Create your views here.

from login.models import UserLogin

# 定义表单模型
class UserLoginForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())


# 最初进入网点, 进行密码登录
def login(request):
    if request.method == 'POST':
        print('开始views.login函数')
        uf = UserLoginForm(request.POST)
        if uf.is_valid():
            # 获取表单密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # 将获取的表单的帐号与密码与数据库中的进行比对。如果成功, 那么进入 index.html 界面。
            user = UserLogin.objects.filter(username__exact=username, password__exact=password)
            if user:
                # return render(request, 'test1/index.html', context)
                # return HttpResponseRedirect(reverse('login'))
                print('密码成功！')
                return afterLogin(request)
            else:
                return render(request, 'login.html', {
                    'welcome': "Welcome to test1/views.login",
                    'login': "fail",
                })
    else:
        uf = UserLoginForm()
        return render(request, 'login.html', {'uf': uf})


def afterLogin(request):
    '''
    登录成功之后, 原来页面的信息变成显示当前能够选择的服务的一个列表, 同一个网址！
    :param request:
    :return:
    '''
    print('调用了 afterLogin 函数')
    return render(request, 'afterLogin.html')


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


