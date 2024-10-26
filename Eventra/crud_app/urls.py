from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_eventos, name='menu_eventos'),
    path('register/', views.registro_usuario, name='registro_usuario')
]