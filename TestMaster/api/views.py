from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
# make json

def hello(request):
    return HttpResponse('hello world!')


@csrf_exempt
def makeBranchJson(request):
    '''
    访问地址： test1/api/makejson/
    用于生成一个 JSON 数据，模拟 TestMaster 返回的 branch 的信息
    :param request:
    :return:
    '''
    print("调用apitest中的makeBranchJson函数")
    data = {
        "meta": {"total": 3},
        "branches": [
            {
                'name': 'testBranchName1',
                'revision': "aaaa",
                'requestid': 101,
                'lasttest': '2010-10-1',
            },
            {
                'name': 'testBranchName2',
                'revision': "bbbb",
                'requestid': 102,
                'lasttest': '2010-10-2',
            },
            {
                'name': 'testBranchName3',
                'revision': "cccc",
                'requestid': 103,
                'lasttest': '2010-10-3',
            }
        ]
    }
    return HttpResponse(json.dumps(data))


@csrf_exempt
def makeMachineJson(request):
    '''
        访问地址： test1/api/makemachinejson/
        用于生成一个 JSON 数据，模拟 TestMaster 返回的 branch 的信息, 包括 机器编号(id)、测试编号(test)、运行状态(status)、运行时间(time)、行驶距离(distance)
        :param request:
        :return:
    '''
    print("调用apitest中的makeMachineJson函数")
    data = {
        "meta": {'total': 3},
        "machines": [
            {
                'name': "bot1",
                'address': "10.0.169.11",
                'requestid': 19,
                "status":"runing",
            },
            {
                'name': "bot2",
                'address': "10.0.169.12",
                'requestid': 20,
                "status":"runing",
            },
            {
                'name': "bot3",
                'address': "10.0.169.13",
                'requestid': 21,
                "status":"runing",
            }
        ]
    }

    return HttpResponse(json.dumps(data))

@csrf_exempt
def makeMachineJson2(request):
    '''
        访问地址： test1/api/makemachinejson/
        用于生成一个 JSON 数据，模拟 TestMaster 返回的 branch 的信息, 包括 机器编号(id)、测试编号(test)、运行状态(status)、运行时间(time)、行驶距离(distance)
        对应 uosWeb 中 sts/views.py 中的 machine2 函数
        :param request:
        :return:
    '''
    print("调用apitest中的makeMachineJson2函数")
    try:
        branchName = request.GET['branchName']
        case = request.GET['case']
    except:
        data = {
            'error': '请求的url有误，其中包含的信息不够'
        }
        return HttpResponse(json.dumps(data))
    else:
        print('从用户那边传过来url中包含的branchName：   ', branchName)
        print('从用户那边传过来url中包含的case：   ', case)
        # 这里就是十分简单的返回数据了，真实情况下应该发送运行指令给下面的 TestWorks, 再收集信息返回
        data = [
            {
                'id': 1001,
                'test': 10001,
                'status': 1,
                'time': 100,
                'distance': 5000,
            },
            {
                'id': 1002,
                'test': 10001,
                'status': 0,
                'time': 102,
                'distance': 5002,
                'error': "lots of words",
            },
            {
                'id': 1003,
                'test': 10003,
                'status': 1,
                'time': 103,
                'distance': 5003,
            }
        ]
        return HttpResponse(json.dumps(data))

@csrf_exempt
def makeCase(request):
    '''
    参照了友志发我的邮件
    访问地址 api/v1/makecase
    :param request:
    :return:
    '''
    data = {
        "meta": {"total": 6},
        "testcases": [
            {"name": 'fromTMname1'},
            {"name": 'fromTMname2'},
            {"name": 'fromTMname3'},
            {"name": 'fromTMname4'},
            {"name": 'fromTMname5'},
            {"name": 'fromTMname6'},
        ]
    }
    return HttpResponse(json.dumps(data))


@csrf_exempt
def makeCompileResult(request):
    '''
    访问地址： test1/api/makecompileresult/
    用于模拟 TestMaster 返回的编译结果, JSON 数据 {'result': 'success/fail', 'error': '...'}
    :param request:
    :return:
    '''
    print("调用apitest中的makeCompileResult函数")
    name = request.GET['branchName']
    if name == 'testBranchName1':
        data = {
            'result': 'fail',
            'error': '调用apitest中的makeCompileResult函数, just a test, should show in the console'
        }
    elif name == 'testBranchName2':
        data = {
            'result': 'success',
            'error': '调用apitest中的makeCompileResult函数, just a test, should show in the console'
        }
    else:
        data = {
            'result': 'fail',
            'error': '调用apitest中的makeCompileResult函数, just a test, should show in the console'
        }
    return HttpResponse(json.dumps(data))
