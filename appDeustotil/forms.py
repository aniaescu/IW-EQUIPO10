from django import forms
from .models import Proyecto, Tarea

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = '__all__'

