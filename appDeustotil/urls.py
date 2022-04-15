from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('proyectos/', views.index_proyecto, name='proyectos'),
    path('tareas/', views.index_tarea, name='tareas'),
    path('tareas/<int:tarea_id>/', views.show_tarea, name='tarea'),
    path('proyectos/<int:proyecto_id>', views.show_proyecto, name='proyecto'),    
]