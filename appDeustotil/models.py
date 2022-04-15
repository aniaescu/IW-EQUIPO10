from django.db import models
from django.forms import EmailField

class Cliente(models.Model):
    Nombre = models.CharField()
    Email = models.EmailField()
    Telefono = models.CharField()

    def __str__(self):
        return self.Nombre

class Empleado(models.Model):
    DNI = models.CharField(max_length=9)
    Nombre = models.CharField()
    Apellidos = models.CharField()
    Email = models.EmailField()
    Telefono = models.IntegerField(max_length=9)

    def __str__(self):
        return self.DNI


class Tarea(models.Model):
    Nombre = models.CharField()
    Descripcion = models.CharField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    responsable = models.ForeignKey(Empleado)
    prioridad = models.CharField(choices=(('Alta'), ('Media'), ('Alta')), default=('Media'))
    estado = models.CharField(choices=(('Abierta'), ('Asignada'), ('En proceso'), ('Finalizada')), default=('Abierta'))
    notas = models.TextField(null=True, blank=True)
    

    def __str__(self):
        return self.Nombre


class Proyecto(models.Model):
    Nombre = models.CharField()
    Descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    Presupuesto = models.IntegerField()
    Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    Reponsable = models.ForeignKey(Empleado)
    Tarea = models.ForeignKey(Tarea)

    def __str__(self):
        return self.Nombre

