from django.shortcuts import render
from django.http import HttpResponse
from .models import Testset, UerLogin

# Create your views here.

# 最初进入网点, 进行密码登录
def login(request):
    userDB = 


# 最初进入网点
def index(request):
    # 从request中获取各个机器的运行状态
    context = {
        'welcome': "Welcome to test1/views.Machines",
        'page1' : "压力测试系统",
        'page2' : "持续集成系统",
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
    context = {
        'welcome': "Welcome to test1/views.build",
    }
    return render(request, 'test1/buildbranch.html', context)

# ex: test1/machines/   由branch页面提交表单后跳转过来
# def machines(request):
#     # 从request中获取各个机器的运行状态, request中有 机器的测试编号, 运行时间, 运行状态, 运行距离等
#     # 如何从 request 中获取这些数据? 并封装成字典的形式?
#     try:
#         testbranch = request.POST['testbranch233']   # name 属性
#         testset = request.POST['testset233']
#         testpatch = request.POST['testpatch233']
#     except(KeyError):
#         return render(request, 'test1/connect.html', {
#             'error_message': "You didn't type the email or password.",
#         })
#     else:
#         context = {
#             'branch': testbranch,
#             'set': testset,
#             'patch': testpatch,
#             'welcome': "Welcome to test1/views.Machines",
#             'range': range(1, 16),
#         }
#         return render(request, 'test1/machines.html', context)
def machines(request):
    context = {
        'welcome': "Weclome to test1/views.machines",
        'range' : range(1, 16),
    }
    return render(request, 'test1/machines.html', context)


#持续集成系统所用的
def machinesCIS(request):
    context = {
        'welcome': "Welcome to test1/views.machinesCIS",
    }
    return render(request, 'test1/machinesCIS.html', context)

