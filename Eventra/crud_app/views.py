from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import RegistroUsuarioForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, logout as auth_logout
from .models import Usuario

# views.py

def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = RegistroUsuarioForm()

    return render(request, 'autenticacion/registro_usuario.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        usuario = Usuario.objects.filter(usuario=username).first()
        if usuario and usuario.check_password(password):
            request.session['user_id'] = usuario.id  # Guarda el usuario en la sesión
            auth_login(request, usuario, backend='crud_app.auth_backend.UsuarioAuthBackend')
            messages.success(request, '¡Inicio de sesión exitoso!')
            return render(request, 'redirect/redirect.html', {'url': 'home'})  # Redirige a la plantilla de redirección
        else:
            messages.error(request, 'Credenciales incorrectas.')

    return render(request, 'autenticacion/login.html')


@login_required
def logout_view(request):
    auth_logout(request)
    return redirect('home')  # Redirige a la vista de login

def home(request):
    return render(request, 'eventra/index.html')


