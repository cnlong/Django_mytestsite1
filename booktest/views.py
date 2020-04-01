from django.shortcuts import render,redirect
from booktest.models import *
from datetime import date
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def index(request):
    """显示图书信息"""
    # 1.查询出所有的图书信息
    books = BookInof.objects.all()
    # 2.使用模板
    return render(request, 'booktest/index.html', {'books': books})


def create(request):
    """新增一本图书"""
    # 1.创建一个BookInfo对象
    b = BookInof()
    b.btitle = '流星蝴蝶剑'
    b.bpub_date = date(1990,1,1)
    # 保存数据
    b.save()
    # # 返回应答，让浏览器返回首页index,也就是重定向
    # return HttpResponse('ok!')
    # return HttpResponseRedirect('/index')
    # 可以通过redirect重定向更方便
    return redirect('/index')


def delete(request, bid):
    """删除图书"""
    # 1.通过bid获取图书对象
    book = BookInof.objects.get(id=bid)
    # 2.删除
    book.delete()
    # 3.重定向到首页
    # return HttpResponseRedirect('/index')
    # 注意这里的重定向的路径和其原来的视图url路径同级，也就是127.0.0.0/delete8 ==》 127.0.0.1/index
    # 如果原来的URL是127.0.0.0/delete/8,对应重定向的是127.0.0.0/delete/index。这样会找不到首页
    return redirect('/index')