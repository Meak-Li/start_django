from django.shortcuts import render, HttpResponse
from django.conf import settings

name = settings.NAME


# Create your views here.
def login(request):
    return HttpResponse("we will welcome!")


def test(request):
    return HttpResponse("one")


def demo(request):
    return HttpResponse("demo")


def demo_id(request, id):
    print(id)
    print(type(id))
    return HttpResponse("success")


def test_converter(request, year):
    return HttpResponse('自定义转换器启动成功')
