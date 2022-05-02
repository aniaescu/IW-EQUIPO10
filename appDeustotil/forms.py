from django import forms
from .models import Proyecto, Tarea, Empleado, Cliente

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
