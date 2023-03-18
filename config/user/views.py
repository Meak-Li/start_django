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


def test_re_path(request, year):
    return HttpResponse(f'test_re_path:{year}------')


def test_month_re_path(request, year, month):
    return HttpResponse(f'test_month_re_path:{year}--{month}------')


def test_repath_standard(request, year):
    return HttpResponse(f'test_repath_standard:{year}')


def get_info(request, page=1):
    return HttpResponse(f"默认值: {page}")


def other_arg(request, info):
    return HttpResponse(f"额外的参数：{info}")
