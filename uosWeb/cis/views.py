from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def indextest(request):
    return HttpResponse('this is cis views.indextest, 下一步是修改 CI 的网站')
