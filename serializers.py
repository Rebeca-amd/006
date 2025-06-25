from rest_framework import serializers
from .models import Producto  # Asegúrate de tener este modelo definido

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'
