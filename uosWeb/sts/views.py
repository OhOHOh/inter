from django.http import HttpResponse
from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
import requests,json, random

from .models import Testcase
# Create your views here.


#
# 到底要不要加 'http://' 要看输入的情况, 后期根据输入的情况再做调整
# 现阶段, 是输入 IP+PORT 的形式, 例如 10.0.169.155:8000, 那么我们在后台的函数中自己加上 'http://'
#

ip_port = ''
caseList_g = []

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
        if ip[0] != 'h':
            ip = 'http://' + ip
        global ip_port
        ip_port = ip                                      # 把用户填写的 IP+PORT 存在全局变量 ip_port 中, 并且确保ip_port 是 end with '/' 的
        url = ip + 'api/v1/branches/'      # url is TestMaster's API, we can get branch info from the url.
        # 从 TM 处获取 branch 的信息
        r = requests.get(url)                    # no more 'try', because we do it before in function tryConnect
        if r.status_code == requests.codes.ok:   # requests.codes.ok = 200
            data = r.json()                      # 取得 branch 数据
            print(data)

            branchNum = data['meta']['total']    # branch 的个数, 目前没有用到
            branchList = data['branches']

            # 如果TM 没有传递给我们 branch 信息的话：
            # if branchList == '':
            #     context = {
            #         'errorBranch': '没有从TestMaster处获得任何branch的信息'
            #     }
            #     return render(request, 'sts/fail.html', context)

            context = {
                'branchfromTM': branchList,
                'TMip': ip,                      # 传递给 connect.html
            }
            return render(request, 'sts/branch.html', context)
        else:  # in case of 404, 404 means TM server does not have the url, but we can access the ip+port
            context = {
                'error_message': '访问地址有误，请检查 TestMaster 后台对应的api接口地址和本页面对应的访问地址！',
                'ip': url,
            }
            return render(request, 'sts/fail.html', context)

    # 用于 branch.html 与 machine.html 的互通
    global ip_port
    print(ip_port)
    url = ip_port + 'api/v1/branches/'
    print(url)
    r = requests.get(url)  # no more 'try', because we do it before in function tryConnect
    if r.status_code == requests.codes.ok:  # requests.codes.ok = 200
        data = r.json()
        print(data)

        branchNum = data['meta']['total']  # branch 的个数, 目前没有用到
        branchList = data['branches']

        context = {
            'branchfromTM': branchList,
            'TMip': ip_port,  # 传递给 connect.html
        }
    return render(request, 'sts/branch.html', context)


def connect(request):
    '''
    被 connect2 代替, 后同
    :param request:
    :return:
    '''
    if request.method == "POST":
        print('connect函数')
        name = request.POST['branchName']
        ip = request.POST['TMip']
        print('从branch.html中传过来的branchName: ', name)
        print('从branch.html中传过来的TMip: ', ip)

        testcase_list = Testcase.objects.order_by('caseName')

        print(testcase_list)

        return render(request, 'sts/connect.html', {
            'branchName': name,
            'TMip': ip+'api/v1/machines/',               # TM 端返回 machine 的信息
            'testcase_list': testcase_list,
        })

    return HttpResponse('views.connect')


def connect2(request):
    '''
    接受从 branch.html 页面传递过来的参数(branchName, ip), 与上一个connect函数不同的是, 要从TM 处请求 case 的名字, 而不是从本地的数据库中获取
    :param request:
    :return:
    '''
    if request.method == "POST":
        print('connect函数')
        name = request.POST['branchName']
        ip = request.POST['TMip']
        print('从branch.html中传过来的branchName: ', name)
        print('从branch.html中传过来的TMip: ', ip)

        # testcase_list = Testcase.objects.order_by('caseName')

        url = ip + 'api/v1/testcases/'
        r = requests.get(url)
        testcase_list = []
        data = r.json()         # 获取传过来的 case 数据

        # 对其进行解析
        caseNum = data['meta']['total']   # 没有用到
        global caseList_g
        caseList = data['testcases']
        caseList_g = caseList
        for item in caseList:
            testcase_list.append(item['name'])

        print(testcase_list)

        return render(request, 'sts/connect.html', {
            'branchName': name,
            'TMip': ip+'api/v1/machines/',           # TM 端返回 machine 的信息
            'testcase_list': testcase_list,
        })

    return HttpResponse('views.connect')


def machine(request):
    if request.method == 'POST':
        url = request.POST['address233']
        case = request.POST['case233']
        patch = request.POST['patch2233']
        branchName = request.POST['branchName']
        print(url)
        print(case)
        print(patch)
        print(branchName)

        r = requests.get(url)
        print(r.json())

        context = {
            'machines': r.json(),
        }
        return render(request, 'sts/machine.html', context)
    return render(request, 'sts/machine.html')


def machine2(request):
    '''
    对def machine的一个改进, 把connect.html中表单的信息也传递给TM！这样TM才能根据传过去的信息来返回具体的值！！！由此看来, machine 函数没有必要了
    要使machine2替代machine, 只需要修改 sts/urls.py 中的 url(r'^machine/$', views.machine, name='machine') 中的 views.machine2 即可
    :param request:
    :return:
    '''
    if request.method == 'POST':
        url = request.POST['address233']
        case = request.POST['case233']
        branchName = request.POST['branchname2233']

        payload = {
            'branchName': branchName,
            'case': case,
        }
        # r = requests.get(url, params=payload)
        r = requests.get(url)
        data = r.json()
        print(data)

        # 对其进行解析
        machineNum = data['meta']['total']
        machineList = data['machines']

        global caseList_g
        id_local = random.randint(1,1000)
        addreq = {"jsonrpc": "2.0", "method": "add",
                  "params": {
                      "requestid": 1,
                      "name": "helloworld",
                      "type": "repo",
                      "branch": branchName,
                      "testcases": case,
                      "properties": {}
                  }, "id": id_local
                  }
        headers = {"content-type": "application/json"}
        try:
            r = requests.post('http://10.0.169.162:8070/api/v1/testrequest', data=json.dumps(addreq), headers=headers)
        except Exception as e:
            print('error %s' % (str(e)))



        context = {
            'machines': machineList,
        }
        return render(request, 'sts/machine.html', context)

    # 用于 branch.html 与 machine.html 的互通, 需要TM那边设置一个api端口
    global ip_port
    url1 = ip_port + 'api/v1/machines/'              # 这里也是一个从 TM 处获取数据的接口
    r = requests.get(url1)
    data = r.json()

    # 对其进行解析
    machineNum = data['meta']['total']
    machineList = data['machines']

    context = {
        'machines': machineList,
    }

    return render(request, 'sts/machine.html', context) # 需要 connect.html 中的表单文件

def ping(request):
    return render(request, 'sts/ping.html')


@csrf_exempt
def tryConnect(request):
    """
    相当于 PING 测试, 用于最初进入 sts 的时候配置 TM 的 url , 用到
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
