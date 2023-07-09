from django.urls import path, include
from rest_framework import routers

from .views import BookTRviewset, RatingViewset, UserViewset

router = routers.DefaultRouter()
router.register('books', BookTRviewset)
router.register('ratings', RatingViewset)
router.register('users', UserViewset)


urlpatterns = [
    path('', include(router.urls)),
]
