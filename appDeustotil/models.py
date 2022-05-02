from django.db import models
from django.forms import EmailField

# Clase cliente
class Cliente(models.Model):
    nombre = models.CharField(max_length=60)
    email = models.EmailField()
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre

# Clase empleado
class Empleado(models.Model):
    dni = models.CharField(max_length=9)
    nombre = models.CharField(max_length=60)
    apellidos = models.CharField(max_length=120)
    email = models.EmailField()
    telefono = models.IntegerField()

    def __str__(self):
        return self.dni

# Clase Tarea
class Tarea(models.Model):
    prioridad_choices =(('Alta', 'Alta'), ('Media', 'Media'), ('Baja', 'Baja'))
    estado_choices = (('Abierta', 'Abierta'), ('Asignada', 'Asignada'), ('En proceso', 'En proceso'), ('Finalizada', 'Finalizada'))

    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=120)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    responsable = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    prioridad = models.CharField(max_length=10, choices= prioridad_choices , default=('Media'))
    estado = models.CharField(max_length=16, choices= estado_choices, default=('Abierta'))
    notas = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.nombre

#Clase Proyecto
class Proyecto(models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.TextField(max_length=120)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    presupuesto = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    reponsable = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre







