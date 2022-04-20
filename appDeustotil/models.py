from django.db import models
from django.forms import EmailField

class Cliente(models.Model):
    nombre = models.CharField()
    email = models.EmailField()
    telefono = models.CharField()

    def __str__(self):
        return self.nombre

class Empleado(models.Model):
    dni = models.CharField(max_length=9)
    nombre = models.CharField()
    apellidos = models.CharField()
    email = models.EmailField()
    telefono = models.IntegerField(max_length=9)

    def __str__(self):
        return self.dni


class Tarea(models.Model):
    nombre = models.CharField()
    descripcion = models.CharField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    responsable = models.ForeignKey(Empleado)
    prioridad = models.CharField(choices=(('Alta'), ('Media'), ('Alta')), default=('Media'))
    estado = models.CharField(choices=(('Abierta'), ('Asignada'), ('En proceso'), ('Finalizada')), default=('Abierta'))
    notas = models.TextField(null=True, blank=True)
    

    def __str__(self):
        return self.nombre


class Proyecto(models.Model):
    nombre = models.CharField()
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    presupuesto = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    reponsable = models.ForeignKey(Empleado)
    tarea = models.ForeignKey(Tarea)

    def __str__(self):
        return self.nombre

