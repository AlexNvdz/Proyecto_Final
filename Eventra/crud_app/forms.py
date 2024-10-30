
# forms.py
from django import forms
from .models import Usuario

class RegistroUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['usuario', 'contraseña', 'correo', 'tipo_usuario']
        widgets = {
            'contraseña': forms.PasswordInput(),
        }
    
    tipo_usuario = forms.ChoiceField(
        choices=Usuario.TIPO_USUARIO,
        widget=forms.RadioSelect,  # Mostrar como selección de radio
        label="Tipo de usuario"
    )
    
    def save(self, commit=True):
        # Usamos la encriptación definida en el modelo
        user = super().save(commit=False)
        user.contraseña = self.cleaned_data["contraseña"]
        if commit:
            user.save()
        return user


