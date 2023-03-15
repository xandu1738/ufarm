from django.urls import path
from .import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_fo/', views.add_fo, name='add_fo'),
    path('add_uf/', views.add_uf, name='add_uf'),
    path('add_activity/', views.add_activity, name='add_activity'),
]
