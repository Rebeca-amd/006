
from django.contrib import admin
from django.urls import path, include  # ← esto es importante

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('GoldenCafe.urls')),  # ← esta línea conecta tu app
]



