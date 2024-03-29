from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('farmers.urls')),
    path('products/', include('products.urls')),
]
