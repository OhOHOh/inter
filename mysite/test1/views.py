from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    # 从request中获取各个机器的运行状态
    context = {
        'welcome': "Welcome to test1/views.Machines",
        'page1' : "压力测试",
        'page2' : "直接查看Machines Info",
    }
    return render(request, 'test1/index.html', context)


def machines(request):
    # 从request中获取各个机器的运行状态, request中有 机器的测试编号, 运行时间, 运行状态, 运行距离等
    # 如何从 request 中获取这些数据? 并封装成字典的形式?
    try:
        testbranch = request.POST['testbranch233']   # name 属性
        testset = request.POST['testset233']
        testpatch = request.POST['testpatch233']
    except(KeyError):
        return render(request, 'test1/branch.html', {
            'error_message': "You didn't type the email or password.",
        })
    else:
        context = {
            'branch': testbranch,
            'set': testset,
            'patch': testpatch,
            'welcome': "Welcome to test1/views.Machines",
            'range': range(1, 16),
        }
        return render(request, 'test1/Machines.html', context)


def branch(request):
    context = {
        'welcome': "Welcome to test1/views.branch, please input",
    }
    return render(request, 'test1/branch.html', context)
