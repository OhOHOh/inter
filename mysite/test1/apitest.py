from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def makeBranchJson(request):
    '''
    访问地址： test1/api/makejson/
    用于生成一个 JSON 数据，模拟 TestMaster 返回的 branch 的信息
    :param request:
    :return:
    '''
    print("调用apitest中的makeBranchJson函数")
    data = [
        {
        'branchName': 'testBranchName1',
        'compileTimes': 100,
        'runTimes': 100,
        'lastCompile': '2010-10-1',
        'lastRun': '2010-10-3',
        },
        {
            'branchName': 'testBranchName2',
            'compileTimes': 200,
            'runTimes': 200,
            'lastCompile': '2020-10-1',
            'lastRun': '2020-10-3',
        },
        {
            'branchName': 'testBranchName3',
            'compileTimes': 300,
            'runTimes': 300,
            'lastCompile': '2030-10-1',
            'lastRun': '2030-10-3',
        }
    ]
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
    data = [
        {
            'id' : 1001,
            'test': 10001,
            'status': 0,
            'time': 100,
            'distance': 5000,
        },
        {
            'id': 1002,
            'test': 10001,
            'status': 0,
            'time': 102,
            'distance': 5002,
        },
        {
            'id': 1003,
            'test': 10003,
            'status': 0,
            'time': 103,
            'distance': 5003,
        }
    ]
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
