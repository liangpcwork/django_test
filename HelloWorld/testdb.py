#!/usr/bin/env python
from django.shortcuts import render
from django.http import HttpResponse
from TestModel.models import Test


def test_db(request):
    # 添加数据
    test1 = Test(name="KD", age=22)
    test1.save()
    return HttpResponse("<p>add data successfully!</p>")

def test_db_get_all(request):
    # 查询数据（过滤， where）
    objects_filter = Test.objects.filter(id=2).first()
    response2 = HttpResponse("<p>get filter: names:%s  ages:%s</p>" % (objects_filter.name, objects_filter.age))
    # 更新数据
    object_get_one = Test.objects.get(id=1)
    object_get_one.name = "Green"
    object_get_one.save()
    response3 = HttpResponse("<p>object_get_one: names:%s  ages:%s</p>" % (object_get_one.name, object_get_one.age))
    # 删除数据
    object_get_one.delete()
    objects_list = Test.objects.all()
    names = ""
    ages = ""
    for obj in objects_list:
        names = names + obj.name
        ages = ages + "#" + str(obj.age)
    response1 = HttpResponse("<p>get all: names:%s  ages:%s</p>" % (names, ages))
    return response1
