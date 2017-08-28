from django.db import models

# Create your models here.

# 在 buildbranch.html 中使用, 存储的是 branch 的5个信息：branch名字(需要传给 TM)、编译次数、最近编译时间、运行次数、最近运行次数
# TM 是根据其中的 branch_name 来选择哪个 branch 来进行操作
class BranchInfo(models.Model):
    branch_name = models.CharField(max_length=100)
    compile_times = models.IntegerField(default=0)
    last_compile = models.DateTimeField(null=True)
    # last_compile = models.CharField(max_length=100)
    run_times = models.IntegerField(default=0)
    last_run = models.DateTimeField(null=True)
    # last_run = models.CharField(max_length=100)

    def __str__(self):
        return self.branch_name

# auto_now=True

# 存放的是 Testcase 的名字, 在 connect.html 中使用
class Testcase(models.Model):
    caseName = models.CharField(max_length=200)
