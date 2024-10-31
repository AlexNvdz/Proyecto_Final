from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_eventos, name='menu_eventos'),
    path('registro/', views.registrar_usuario, name='registro'),
    path('login/', views.login_view, name='login')
]