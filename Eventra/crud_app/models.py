from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.hashers import make_password, check_password

class Usuario(models.Model):
    TIPO_USUARIO = [
        ('cliente', 'Cliente'),
        ('administrativo', 'Administrativo')
    ]

    usuario = models.CharField(max_length=150, unique=True)
    contraseña = models.CharField(max_length=258)  # Almacenará la contraseña encriptada
    correo = models.EmailField(unique=True)
    tipo_usuario = models.CharField(max_length=20, choices=TIPO_USUARIO)
    last_login = models.DateTimeField(auto_now=True)  # Campo para registrar el último inicio de sesión

    def save(self, *args, **kwargs):
        # Encriptar la contraseña antes de guardar si el usuario es nuevo
        if not self.pk:
            self.contraseña = make_password(self.contraseña)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        return check_password(raw_password, self.contraseña)
    
    @property
    def is_authenticated(self):
        return True








####CAMBIOS########

from datetime import datetime
import os

def upload_to(instance, filename):
    # Cambiar el nombre de la imagen con la fecha y el ID del evento
    fecha = datetime.now().strftime("%Y%m%d")
    filename_base, filename_ext = os.path.splitext(filename)
    return f'{fecha}_{instance.nombre}{filename_ext}'

class Eventos(models.Model):
    CIUDADES = [
        ('Montería', 'Montería'),
        ('Bogotá', 'Bogotá'),
        ('Medellín', 'Medellín'),
        ('Cali', 'Cali'),
        ('Cartagena', 'Cartagena'),
    ]
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='eventos')  # Relación uno a muchos
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=300)
    ubicacion = models.CharField(max_length=50, choices=CIUDADES)
    descripcion = models.TextField()
    precio_renta = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to=upload_to)

    def __str__(self):
        return self.nombre
    




    #### CAMBIOS NUEVOS ####


class Reserva(models.Model):
    usuario_reserva = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, related_name="reservas_realizadas"
    )  # Usuario que hace la reserva
    evento = models.ForeignKey(
        Eventos, on_delete=models.CASCADE, related_name="reservas"
    )  # Evento reservado
    fecha = models.DateField()
    hora = models.TimeField()
    numero_invitados = models.PositiveIntegerField()
    duracion = models.PositiveIntegerField(help_text="Duración en horas")
    correo_usuario = models.EmailField()

    # Opcional: agregar timestamp
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reserva de {self.usuario_reserva.nombre} para {self.evento.nombre}"