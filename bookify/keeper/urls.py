from django.contrib import admin
from django.urls import path, include
from .views import function_view, ClassView, template_view, BookViewSet, CharacterViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register('books', BookViewSet)
router.register('characters', CharacterViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('function/', function_view),
    path('class/', ClassView.as_view()),
    path('template/', template_view),
]
