# Generated by Django 5.1.2 on 2024-10-30 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=150, unique=True)),
                ('contraseña', models.CharField(max_length=258)),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('tipo_usuario', models.CharField(choices=[('cliente', 'Cliente'), ('administrativo', 'Administrativo')], max_length=20)),
            ],
        ),
    ]