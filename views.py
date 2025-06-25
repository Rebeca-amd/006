from django.shortcuts import render

print(">>> views.py CARGADO desde:", __file__)  # Línea que estamos agregando

from rest_framework import viewsets
from GoldenCafe.models import Producto
from .serializers import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer



