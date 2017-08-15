from django.db import models
from django.utils import timezone
import datetime, time


# Create your models here.

class Machine(models.Model):
    # 机器是否在运行
    isAlive = models.BooleanField(default=False)
    # 机器运行时间, 当前时间-开机时间
    beginTime = models.DateTimeField(default=timezone.now)
    nowTime = models.DateTimeField('当前时间', auto_now=True)
    workTime = models.IntegerField('工作时间', default=0)
    # TestMaster 返回的信息
    text = models.TextField(default="")
    name = models.CharField(max_length=200)

    def cal_worktime(self):
        if self.isAlive:
            self.workTime = (self.nowTime - self.beginTime).seconds
            # 将秒数转成time类型，再显示
            workTimeHour = self.workTime % 3600
            workTimeMin = (self.workTime / 3600) % 60
            workTimeSec = (self.workTime / 3600) / 60
        else:
            self.workTime = 0
            # 显示 '-' 表示机器出现故障，并且将 self.text（出错信息） 显示在网页上

    def __str__(self):
        return self.name


# 出错的时候记录对应的 machine 的出错记录
class Errortext(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)

    errorid = Machine.name
    errortext = models.TextField()

    def __str__(self):
        return self.errorid

class Testset(models.Model):
    setName = models.CharField(max_length=200)

    def __str__(self):
        return self.setName

class UserLogin(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username

# 在 buildbranch.html 中使用, 存储的是 branch 的5个信息：branch名字(需要从TM中传过来)、编译次数、最近编译时间、运行次数、最近运行次数
class BranchInfo(models.Model):
    branch_name = models.CharField(max_length=100)
    compile_times = models.IntegerField(default=0)
    last_compile = models.DateTimeField(auto_now=True)
    run_times = models.IntegerField(default=0)
    last_run = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.branch_name

