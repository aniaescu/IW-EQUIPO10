from django.db import models

class Tarea(models.Model):
    Nombre = models.CharField()
    Descripcion = models.CharField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    responsable = models.ForeignKey(Empleado)
    prioridad = models.CharField()
    estado = models.CharField()
    notas = models.CharField()

    def __str__(self):
        return self.nombre


class Proyecto(models.Model):
    Nombre = models.CharField()
    Descripcion = models.CharField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    Presupuesto = models.IntegerField()
    Cliente = models.ManyToManyField(Cliente)
    Tareas = models.ForeignKey(Tarea)
    Reponsable = models.ForeignKey(Empleado)

    def __str__(self):
        return self.Nombre

