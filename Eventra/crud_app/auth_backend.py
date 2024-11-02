from django.contrib.auth.backends import BaseBackend
from django.utils import timezone
from .models import Usuario

class UsuarioAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            usuario = Usuario.objects.get(usuario=username)
            if usuario.check_password(password):
                usuario.last_login = timezone.now()  # Actualiza el último inicio de sesión
                usuario.save()
                return usuario
        except Usuario.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Usuario.objects.get(pk=user_id)
        except Usuario.DoesNotExist:
            return None
