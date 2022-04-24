from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='pagPrincipal'),
    path('proyectos/', views.ProyectoListView.as_view(), name='proyectos_list'),
    path('tareas/', views.TareaListView.as_view(), name='tarea_list'),
    path('tareas/<int:pk>/', views.TareaDetailView.as_view(), name='tarea'),
    path('proyectos/<int:pk>', views.ProyectoDetailView.as_view(), name='proyecto'),    
    path('proyectos/create/', views.CreateProyectoView.as_view(), name = 'proyecto_create'),
    path('tareas/create/', views.CreateTareaView.as_view(), name = 'tarea_create'),
]