from multiprocessing import context
from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect

from appDeustotil.models import Proyecto, Tarea
from .forms import ProyectoForm, TareaForm
from django.views import View

# Create your views here.

def index(request):
    return render(request, 'pagPrincipal.html')

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
    proyecto = get_object_or_404(Proyecto, pk=proyecto_id)
    context = {'proyecto': proyecto}
    return render(request, 'proyecto.html', context)

class CreateProyectoView(View):
    # Llamada para mostrar la página con el formulario de creación al usuario
    def get(self, request, *args, **kwargs):
        form = ProyectoForm()
        context = {
            'form': form,
            'titulo_pagina': 'Publicar nuevo proyecto'
        }
        return render(request, 'proyecto_create.html', context)

    # Llamada para procesar la creación de la noticia
    def post(self, request, *args, **kwargs):
        form = ProyectoForm(request.POST)
        if form.is_valid(): # is_valid() deja los datos validados en el atributo cleaned_data
            # noticia = Noticia()

            # noticia.titular = form.cleaned_data['titular']
            # noticia.descripcion = form.cleaned_data['descripcion']
            # noticia.medio = form.cleaned_data['medio']
            # noticia.fecha = form.cleaned_data['fecha']
            # noticia.enlace = form.cleaned_data['enlace']
            # noticia.categoria = form.cleaned_data['categoria']
            # noticia.save()

            form.save() # Abreviación de lo anterior

            # Volvemos a la lista de noticias
            return redirect('proyectos')
        # Si los datos no son válidos, mostramos el formulario nuevamente indicando los errores
        return render(request, 'proyecto_create.html', {'form': form})

class CreateTareaView(View):
    # Llamada para mostrar la página con el formulario de creación al usuario
    def get(self, request, *args, **kwargs):
        form = TareaForm()
        context = {
            'form': form,
            'titulo_pagina': 'Publicar nueva tarea'
        }
        return render(request, 'tarea_create.html', context)

    # Llamada para procesar la creación de la noticia
    def post(self, request, *args, **kwargs):
        form = TareaForm(request.POST)
        if form.is_valid(): # is_valid() deja los datos validados en el atributo cleaned_data
            # noticia = Noticia()

            # noticia.titular = form.cleaned_data['titular']
            # noticia.descripcion = form.cleaned_data['descripcion']
            # noticia.medio = form.cleaned_data['medio']
            # noticia.fecha = form.cleaned_data['fecha']
            # noticia.enlace = form.cleaned_data['enlace']
            # noticia.categoria = form.cleaned_data['categoria']
            # noticia.save()

            form.save() # Abreviación de lo anterior

            # Volvemos a la lista de noticias
            return redirect('tareas')
        # Si los datos no son válidos, mostramos el formulario nuevamente indicando los errores
        return render(request, 'tarea_create.html', {'form': form})        