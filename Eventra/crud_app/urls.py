from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("registro/", views.registrar_usuario, name="registro"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("home/", views.home, name="home"),


    #cambios
     path("registrar_evento/", views.registrar_evento, name="registrar_evento"),
     path('dashboard/eventos/', views.dashboard, name='dashboard'),
     path('sala/<int:evento_id>/', views.sala_detalles, name='sala_detalles'),
     path('dashboard/reservas/', views.administrar_reservas, name='administrar_reservas'),
     path('evento/eliminar/<int:evento_id>/', views.eliminar_evento, name='eliminar_evento'),
     path('reserva/eliminar/<int:reserva_id>/', views.eliminar_reserva, name='eliminar_reserva'),
     path('editar_evento/<int:evento_id>/', views.editar_evento, name='editar_evento'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
