from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import requests

# Create your views here.

ip_g = ''

def index(request):
    '''
    在通过密码登录的那个界面上点击“持续集成系统”, 就调用这个函数, 跳转到 .../cis/  网址
    配置一些信息, 主要是配置 TM 的地址
    :param request:
    :return:
    '''
    # return HttpResponse('sts.views.index')
    return render(request, 'cis/index.html')


def machine(request):
    '''
    主要是获取从 cis：index 中传过来的 ip+port, 将这个地址存储在全局变量 ip_g 中
    :param request: post, 'TMurl'
    :return:
    '''
    if request.method == 'POST':
        global ip_g
        ip_g = request.POST['TMurl']
        if ip_g[-1] != '/':
            ip_g = ip_g + '/'
        return render(request, 'cis/machine.html')




@csrf_exempt
def tryConnect(request):
    """
    相当于 PING 测试, 用于最初进入 sts 的时候配置 TM 的 url , 用到
    通过访问 url: /sts/api/tryconnect 来获取函数的执行, 测试地址里填写的是 IP+PORT, 对于最后有没有加上 '/', 对测试没有影响
    在页面 connect.html 中的 connectTestMaster 函数中引用的 API
    :return:
    """
    if request.method == 'POST':  # 测试地址里填写的是 IP + port, 而这个函数我们需要添加 'http://' 的头
        ip = request.POST.get('ip')
        url = 'http://' + ip
        print(url)
        try:
            r = requests.get(url)
        except:
            print('connect fail')
            return HttpResponse('0')
        else:
            print('connect success')
            return HttpResponse('1')

def getMachine(request):
    global ip_g
    url = 'http://' + ip_g + 'api/v1/makemachinejson/'
    r = requests.get(url)

    context = {
        'machines': r.json()
    }

    return render(request, 'cis/machine.html', context)
