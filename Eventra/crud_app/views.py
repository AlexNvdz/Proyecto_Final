from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

# Create your views here.
def menu_eventos(request):
    return render(request, 'crud_app/index.html')