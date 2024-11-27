# blog/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet , CategoryViewSet

router = DefaultRouter()
router.register(r'blogs', BlogViewSet)
# for category
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
