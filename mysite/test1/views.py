from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import requests

from .models import Testset, UserLogin, BranchInfo
from django import forms
import json
import telnetlib


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
                    'welcome': "Welcome to test1/views.login",
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
    首先, 接受从 connect.html 界面上传过来的表单数据, 将其中的 测试集名称显示在本页面( buildbranch.html )上
    第二, 使用 requests 来从 TestMaster 中获取 BranchInfo 的信息, 返回JSON 中的 key 暂定为 branchName, compileTimes, runTimes, lastCompile, lastRun 这5个
        并将 JSON 数据封装在 context 中, 一起渲染 buildbranch.html
    :param request:
    :return:
    """
    print('进入 buildbranch 函数')
    try:
        testaddress = request.POST['testaddress233']
        testset = request.POST['testset233']
        testpatch = request.POST['testpatch233']
    except(KeyError):
        context = {'error_message': "表单中的<input>中name属性设置的不匹配或者表单信息没有填写完整"}
        return fail(request, context)  # 将'失败'后返回的'失败界面'并显示'失败信息' 的行为封装成一个独立的函数 fail
    else:
        url = 'http://' + testaddress + '/test1/api/makebranchjson/'  # 最后的　/ 要记得添加！
        print(url)
        r = requests.get(url) # 从 TestMaster 的 REST API 中获取 JSON 数据
        data = r.json()
        print(data)
        print(data[0]['branchName'])
        context = {
            'welcome': "Welcome to test1/views.build",
            'address': testaddress,
            'set': testset[:-2],  # 删去最后2个字符 ', '
            'patch': testpatch,
            'branchfromTM': data,
        }
        print('表单传过来的测试集:  ' + testset)
        print('表单传过来的ip地址:  ' + context['address'])
        return render(request, 'test1/buildbranch.html', context)


def machines(request):
    '''
    在 buildbranch/html 中点击 "运行" 按钮, 转到这个地址, 也要从 TestMaster 中获取机器的运行情况
    :param request:
    :return:
    '''
    context = {
        'welcome': "Welcome to test1/views.machines",
        'range': range(1, 16),
    }
    return render(request, 'test1/machines.html', context)


# 持续集成系统所用的
def machinesCIS(request):
    context = {
        'welcome': "Welcome to test1/views.machinesCIS",
    }
    return render(request, 'test1/machinesCIS.html', context)


# 不是 视图函数
def fail(request, context):
    return render(request, 'test1/fail.html', context)


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

@csrf_exempt
def tryConnect(request):
    """
    通过访问 url: test1/api/connect/ 来获取函数的执行, 测试地址里填写的是 IP+PORT
    在页面 connect.html 中的 connectTestMaster 函数`中引用的 API
    :return:
    """
    # if request.method == 'POST':
    #     ip = request.POST.get('ip')
    #     print(ip)
    #     try:
    #         telnetlib.Telnet(ip, port='8000', timeout=20)
    #     except:
    #         print('connect fail')
    #         return HttpResponse('0')
    #     else:
    #         print('connect success')
    #         return HttpResponse('1')
    if request.method == 'POST':  # 测试地址里填写的是 IP + port
        ip = request.POST.get('ip')
        if ip[0] != 'h':
            ip = 'http://' + ip
        url = ip
        try:
            r = requests.get(url)
        except:
            print('connect fail')
            return HttpResponse('0')
        else:
            print('connect success')
            return HttpResponse('1')




def connectserver(request): #162
    print('connectser')
    url = 'http://10.0.169.203:8070/api/v1/hello/'
    r = requests.get(url)
    data = r.text
    context = {
        'welcome': "Welcome to wsgi test",
    }
    # return HttpResponse(data)
    return render(request, 'test1/wsgi.html', context)

def ping(request):
    return render(request, 'test1/ping.html')

@csrf_exempt
def tryPing(request):
    if request.method == 'POST':  # 测试地址里填写的是 IP + port
        ip = request.POST.get('ip')
        if ip[0] != 'h':
            ip = 'http://' + ip
        url = ip
        try:
            r = requests.get(url)
        except:
            context = {
                'result': '0',
                'error': "just a test",
            }
            # response = HttpResponse()
            # response['result'] = '0'
            # response['error'] = "just a test"
            print('connect fail')
            # return HttpResponse('0')
            return HttpResponse(json.dumps(context))
        else:
            context1 = {
                'result': '1',
                'headers': str(r.headers),
                'status_code': r.status_code,
                'content': r.text,
                'protocol': str(r.request),
            }
            print('headers: ', r.headers)
            print('status_code: ', r.status_code)
            print('content: ', r.text)
            print('protocol：', r.request)
            print('connect success')
            # return HttpResponse('1')
            return HttpResponse(json.dumps(context1))
