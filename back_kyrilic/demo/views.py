from django.shortcuts import render
from django.http import HttpResponse


def kyrilic(request):
    return HttpResponse('demo first view ')
