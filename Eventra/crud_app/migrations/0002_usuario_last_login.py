# Generated by Django 5.1.2 on 2024-11-01 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='last_login',
            field=models.DateTimeField(auto_now=True),
        ),
    ]