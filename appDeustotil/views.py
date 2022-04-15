from multiprocessing import context
from django.shortcuts import get_list_or_404, get_object_or_404, render

from appDeustotil.models import Proyecto, Tarea

# Create your views here.

def index_proyecto(request):
    proyectos = get_list_or_404(Proyecto.objects.order_by('fecha_inicio'))
    context = {'lista_proyectos': proyectos}
    return render(request, 'proyectos.html', context)

def index_tarea(request):
    tareas = get_list_or_404(Tarea.objects.order_by('fecha_inicio'))
    context = {'lista_tareas': tareas}
    return render(request, 'tareas.html', context)

def show_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id)
    context = {'tarea': tarea}
    return render(request, 'tarea.html', context)

def show_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Tarea, pk=proyecto_id)
    context = {'proyecto': proyecto}
    return render(request, 'proyecto.html', context)