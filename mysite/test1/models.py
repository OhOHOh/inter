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