from email.policy import default
from django import forms
from .models import Proyecto, Tarea, Empleado, Cliente, Contacto

# Forms creados para poder realizar el formulario.
# Form Proyecto
class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'

# Form Tarea
class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = '__all__'

# Form Empleado
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'

# Form Cliente
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

# Form Contacto
class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'

# Form login
class LoginForm(forms.Form):
    nombre = forms.CharField(label='Introduce tu nombre', max_length=100)
    contraseña = forms.CharField(label='Introduce tu contraseña', max_length=7)

