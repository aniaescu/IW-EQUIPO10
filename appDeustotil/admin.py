from django.contrib import admin
from .models import Cliente, Empleado, Proyecto, Tarea
admin.site.register(Tarea)
admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(Proyecto)
# Register your models here.
