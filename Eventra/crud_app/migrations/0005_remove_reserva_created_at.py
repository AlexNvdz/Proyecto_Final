# Generated by Django 5.1.2 on 2024-11-18 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud_app', '0004_reserva'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='created_at',
        ),
    ]