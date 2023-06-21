from django.contrib import admin
from django.urls import path, include
from .views import function_view, ClassView

urlpatterns = [
    path('function/', function_view),
    path('class/', ClassView.as_view())
]
