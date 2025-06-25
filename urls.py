# GoldenCafe/urls.py
from django.urls import re_path, include
from rest_framework.routers import SimpleRouter
from .views import ProductoViewSet

router = SimpleRouter()
router.register(r'productos', ProductoViewSet)

urlpatterns = [
    re_path(r'', include(router.urls)),
]

