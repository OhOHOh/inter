#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-07-25 10:50:33
# @Author  : Weizhong Tu (mail@tuweizhong.com)
# @Link    : http://www.tuweizhong.com

import os
import json
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

BASE_DIR = settings.BASE_DIR  # 项目目录
# 假设图片放在static/pics/里面
PICS = os.listdir(os.path.join(BASE_DIR, 'common_static/pics'))

print PICS  # 启动时终端上可以看到有哪些图片，我只放了一张，测试完后这一行可以删除


def index(request):
    return render(request, 'index.html')


def get_pic(request):
    color = request.GET.get('color')
    number = request.GET.get('number')
    name = '{}_{}'.format(color, number)

    # 过滤出符合要求的图片，假设是以输入的开头的都返回
    result_list = filter(lambda x: x.startswith(name), PICS)

    print 'result_list', result_list

    return HttpResponse(
        json.dumps(result_list),
        content_type='application/json')
