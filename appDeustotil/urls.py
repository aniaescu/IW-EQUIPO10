from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='pagPrincipal'),
    path('proyectos/', views.index_proyecto, name='proyectos'),
    path('tareas/', views.index_tarea, name='tareas'),
    path('tareas/<int:tarea_id>/', views.show_tarea, name='tarea'),
    path('proyectos/<int:proyecto_id>', views.show_proyecto, name='proyecto'),    
    path('proyectos/create/', views.CreateProyectoView.as_view(), name = 'proyecto_create'),
    path('tareas/create/', views.CreateTareaView.as_view(), name = 'tarea_create'),
]