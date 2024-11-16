
# Register your models here.
# admin.py
from django.contrib import admin
from .models import Usuario, Eventos

admin.site.register(Usuario)
admin.site.register(Eventos)
