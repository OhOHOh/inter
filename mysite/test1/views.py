from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
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
        url = 'http://' + testaddress + ':8000/test1/api/makejson/'  # 最后的　/ 要记得添加！
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
    通过访问 url: test1/api/connect/ 来获取函数的执行
    在页面 connect.html 中的 connectTestMaster 函数中引用的 API
    :return:
    """
    if request.method == 'POST':
        ip = request.POST.get('ip')
        print(ip)
        try:
            telnetlib.Telnet(ip, port='8000', timeout=20)
        except:
            print('connect fail')
            return HttpResponse('0')
        else:
            print('connect success')
            return HttpResponse('1')
    return render(request, 'test1/connect.html')

@csrf_exempt
def makeJson(request):
    '''
    访问地址： test1/api/makejson/
    用于生成一个 JSON 数据，模拟 TestMaster 返回的 branch 的信息
    :param request:
    :return:
    '''
    print("调用views中的makeJson函数")
    data = [{
        'branchName': 'testBranchName1',
        'compileTimes': 100,
        'runTimes': 100,
        'lastCompile': '2020-10-1',
        'lastRun': '2020-10-3',
    },
        {
            'branchName': 'testBranchName2',
            'compileTimes': 200,
            'runTimes': 200,
            'lastCompile': '2030-10-1',
            'lastRun': '2030-10-3',
        }]
    return HttpResponse(json.dumps(data))

@csrf_exempt
def displayJson(request):
    ''' 弃用！！！
    访问地址：/test1/api/displayjson
    当 buildbranch.html 界面获取到来自 TestMaster 的json数据时, 将数据传到此处，再将数据传到网页!就可以使用 Django 的模板文法
    (学艺不精，无法在html界面中直接用JS来循环访问数组的布局, 只能采取这种方式, 希望以后能改进!)
    :param request:
    :return:
    '''
    print('displayJson函数已经开始访问')
    if request.method == 'POST':
        data = request.POST.get('dataObject')
        print(data)
        print(json.dumps(data))
        return render(request, 'test1/buildbranch.html', {
            'datajson': json.dumps(data)
        })
        #return HttpResponse(data)
