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
        if ip[-1] != '/':                                 # make sure ip end with '/'
            ip = ip + '/'
        url = 'http://' + ip + 'api/v1/makebranchjson/'   # url is TestMaster's API, we can get branch info from the url.
        r = requests.get(url)                    # no more 'try', because we do it before in function tryConnect
        if r.status_code == requests.codes.ok:   # requests.codes.ok = 200
            data = r.json()
            print(data)
            context = {
                'branchfromTM': data,
            }
            return render(request, 'sts/branch.html', context)
        else:  # in case of 404, 404 means TM server does not have the url, but we can access the ip+port
            context = {
                'error_message': '访问地址有误，请检查 TestMaster 后台对应的api接口地址和本页面对应的访问地址！',
                'ip': ip,
            }
            return render(request, 'sts/fail.html', context)
    return render(request, 'sts/branch.html')



def connect(request):
    if request.method == "POST":
        print('connect函数')
        name = request.POST['branchName']
        print(name)

        return render(request, 'sts/connect.html', {
            'branchName': name
        })

    return HttpResponse('views.connect')



@csrf_exempt
def tryConnect(request):
    """
    相当于 PING 测试
    通过访问 url: /sts/api/tryconnect 来获取函数的执行, 测试地址里填写的是 IP+PORT, 对于最后有没有加上 '/', 对测试没有影响
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
        print(url)
        try:
            r = requests.get(url)
        except:
            print('connect fail')
            return HttpResponse('0')
        else:
            print('connect success')
            return HttpResponse('1')
