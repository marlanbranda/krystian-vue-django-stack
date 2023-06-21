from django.urls import path
from .views import DemoView, kyrilic, template_func


urlpatterns = [
    path('', kyrilic),
    path('class/', DemoView.as_view()),
    path('templates/', template_func),
]
