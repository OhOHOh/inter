from django.http import HttpResponse
from django.shortcuts import render

from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
import requests

# Create your views here.


#
# 到底要不要加 'http://' 要看输入的情况, 后期根据输入的情况再做调整
# 现阶段, 是输入 IP+PORT 的形式, 例如 10.0.169.155:8000, 那么我们在后台的函数中自己加上 'http://'
#

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
    if request.method == 'POST':
        ip = request.POST['TMurl']
        url = 'http://' + ip + ''   # ip 后面加上去的就是指 TM 的 api 接口
        r = requests.get(url)       # 这里不需要再 try 了, 因为之前已经做过了 PING 测试
        if r.status_code == requests.codes.ok:
            print(requests.codes.ok)
            data = r.json()
            print(data)
            return render(request, 'sts/branch.html', {'data': data})
        else:  # 以防万一出现 404, 意味着 TM 服务器没有对应的网址, 即 TM 后台没有对应的接口, 一种可能是 ip 后面的东西写错, 另一种可能是 TM 后台的 API 地址写错
            context = {
                'error_message': '访问地址有误，请检查 TestMaster 后台对应的api接口地址和本页面对应的访问地址！',
                'url': url
            }
            return render(request, 'sts/fail.html', context)



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
    相当于 PING 测试
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
