from django.http import HttpResponse
from django.shortcuts import render

from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
import requests

# Create your views here.

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



@csrf_exempt
def tryConnect(request):
    """
    通过访问 url: /sts/api/tryconnect 来获取函数的执行, 测试地址里填写的是 IP+PORT
    在页面 connect.html 中的 connectTestMaster 函数中引用的 API
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
    if request.method == 'POST':  # 测试地址里填写的是 IP + port, 而这个函数我们需要添加 'http://' 的头
        ip = request.POST.get('ip')
        url = 'http://' + ip
        try:
            r = requests.get(url)
        except:
            print('connect fail')
            return HttpResponse('0')
        else:
            print('connect success')
            return HttpResponse('1')
