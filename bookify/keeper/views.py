from django.shortcuts import render, HttpResponse


def foo(request):
    return HttpResponse('foo')
