from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import RegistroUsuarioForm, EventoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, logout as auth_logout
from .models import Usuario, Eventos



def registrar_usuario(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")  # Redirige a la página index
    else:
        form = RegistroUsuarioForm()

    return render(request, "autenticacion/registro_usuario.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        usuario = Usuario.objects.filter(usuario=username).first()
        if usuario and usuario.check_password(password):
            request.session["user_id"] = usuario.id  # Guarda el usuario en la sesión
            auth_login(
                request, usuario, backend="crud_app.auth_backend.UsuarioAuthBackend"
            )
            return render(
                request, "redirect/redirect.html", {"url": "index"}
            )  # Redirige a la plantilla de redirección
        else:
            messages.error(request, "Credenciales incorrectas.")

    return render(request, "autenticacion/login.html")


@login_required
def logout_view(request):
    auth_logout(request)
    return redirect("index")  # Redirige a la página index


def index(request):
    return render(request, "eventra/index.html")

def home(request):
    eventos = Eventos.objects.all()
    return render(request, 'eventra/home.html', {'eventos': eventos})

def salaDetalles(request):
    return render(request, "eventra/salaDetalles.html")






########### Cambios #############

@login_required
def registrar_evento(request):
    usuario_actual = request.user  # Obtén el usuario autenticado

    if usuario_actual.tipo_usuario != 'administrativo':
        messages.error(request, "No tienes permisos para registrar eventos.")
        return redirect('home')  # Redirige a home si no es administrativo

    if request.method == "POST":
        form = EventoForm(request.POST, request.FILES)
        if form.is_valid():
            # Crea el evento asociado al usuario actual
            evento = form.save(commit=False)
            evento.usuario = usuario_actual  # Relaciona el evento con el usuario actual
            evento.save()
            
            messages.success(request, "Evento registrado exitosamente.")
            return redirect('dashboard')  # Redirige al dashboard o a otra página
        else:
            messages.error(request, "Error al registrar el evento. Revisa el formulario.")
    else:
        form = EventoForm()  # Formulario vacío para GET

    return render(request, "eventra/registro_evento.html", {"form": form})



"""@login_required
def dashboard(request):
    usuario_actual = request.user

    if usuario_actual.tipo_usuario != 'administrativo':
        return redirect('home')  # Redirige si no es administrativo

    # Obtener los eventos asociados al usuario actual
    eventos = Eventos.objects.filter(usuario=usuario_actual)

    return render(request, 'eventra/dashboard.html', {'eventos': eventos})
"""

@login_required
def dashboard(request):
    usuario_actual = request.user

    if usuario_actual.tipo_usuario != 'administrativo':
        return redirect('home')  # Redirige si no es administrativo
    
    eventos = Eventos.objects.filter(usuario=usuario_actual)

    return render(request, "eventra/dashboard.html", {
        "eventos": eventos,
        "usuario_actual": usuario_actual,
        "messages": messages.get_messages(request),  # Obtén los mensajes para mostrarlos
    })