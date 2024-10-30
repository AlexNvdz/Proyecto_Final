from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import RegistroUsuarioForm

# Create your views here.

# views.py

def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu_eventos')  # Redirige a la página de login o donde prefieras
    else:
        form = RegistroUsuarioForm()
    
    return render(request, 'crud_app/registro_usuario.html', {'form': form})


def menu_eventos(request):
    return render(request, 'crud_app/index.html')

