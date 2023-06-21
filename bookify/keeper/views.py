from django.shortcuts import render, HttpResponse

from django.views import View

class ClassView(View):

    def get(request):
        return HttpResponse('this is by class View ')


def function_view(request):
    return HttpResponse('foo')
