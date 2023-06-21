from django.urls import path
from . import views
from .views import DemoView

urlpatterns = [
    path('', views.kyrilic),
    path('class/', DemoView.as_view()),
]