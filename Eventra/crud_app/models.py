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
