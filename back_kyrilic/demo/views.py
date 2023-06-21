from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class DemoView(View):

    def get(self, request):
        return HttpResponse('this view achieved by django View Class ')


def kyrilic(request):
    return HttpResponse('demo first view ')
