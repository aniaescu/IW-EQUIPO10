from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='pagPrincipal'),
    path('proyectos/', views.ProyectoListView.as_view(), name='proyecto_list'),
    path('tareas/', views.TareaListView.as_view(), name='tarea_list'),
    path('empleados/', views.EmpleadoListView.as_view(), name='empleado_list'),
    path('tareas/<int:pk>/', views.TareaDetailView.as_view(), name='tarea'),
    path('proyectos/<int:pk>/', views.ProyectoDetailView.as_view(), name='proyecto'),
    path('empleados/<int:pk>/', views.EmpleadoDetailView.as_view(), name='empleado'),    
    path('proyectos/create/', views.CreateProyectoView.as_view(), name = 'proyecto_create'),
    path('tareas/create/', views.CreateTareaView.as_view(), name = 'tarea_create'),
    path('empleados/create/', views.CreateEmpleadoView.as_view(), name = 'empleado_create'),
    path('proyectos/delete/<int:pk>/', views.ProyectoDelete, name = 'proyecto_delete'),
    path('tareas/delete/<int:pk>/', views.TareaDelete, name = 'tarea_delete'),
    path('empleados/delete/<int:pk>/', views.EmpleadoDelete, name = 'empleado_delete'),
    path('proyectos/<int:pk>/modificar/', views.ProyectoModificar.as_view(), name = 'proyecto_modificar'),
    path('tareas/<int:pk>/modificar/', views.TareaModificar.as_view(), name = 'tarea_modificar'),
    path('empleados/<int:pk>/modificar/', views.EmpleadoModificar.as_view(), name = 'empleado_modificar')
]