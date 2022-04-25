from multiprocessing import context
from django.shortcuts import  render, redirect, get_object_or_404

from appDeustotil.models import Proyecto, Tarea
from .forms import ProyectoForm, TareaForm
from django.views import View
from django.views.generic import ListView, DetailView

# Create your views here.

def index(request):
    return render(request, 'pagPrincipal.html')

class TareaListView(ListView):
    model = Tarea
    queryset = Tarea.objects.order_by('fecha_inicio')
    template_name = "tarea_list.html"

    def get_context_data(self, **kwargs):
        context = super(TareaListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Listado de Tareas'
        return context

class ProyectoListView(ListView):
    model = Proyecto
    queryset = Proyecto.objects.order_by('fecha_inicio')
    template_name = "proyecto_list.html"

    def get_context_data(self, **kwargs):
        context = super(ProyectoListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Listado de Proyectos'
        return context

class TareaDetailView(DetailView):
    model = Tarea
    template_name = 'tarea.html'

    def get_context_data(self, **kwargs):
        context = super(TareaDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalle de la tarea'
        return context

class ProyectoDetailView(DetailView):
    model = Proyecto
    template_name = 'proyecto.html'

    def get_context_data(self, **kwargs):
        context = super(ProyectoDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalle del proyecto'
        return context        

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
          
            form.save() # Abreviación de lo anterior

            # Volvemos a la lista de noticias
            return redirect('proyecto_list')
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
            

            form.save() # Abreviación de lo anterior

            # Volvemos a la lista de noticias
            return redirect('tarea_list')
        # Si los datos no son válidos, mostramos el formulario nuevamente indicando los errores
        return render(request, 'tarea_create.html', {'form': form})  

def ProyectoDelete(request, pk):
#    proyect = get_object_or_404(Proyecto, id = pk)
#    proyect.delete()
    Proyecto.objects.filter(id = pk).delete()

    return redirect('proyecto_list')

def TareaDelete(request, pk):
#    tare = get_object_or_404(Tarea, id = pk)
#    tare.delete()
    Tarea.objects.filter(id = pk).delete()

    return redirect('tarea_list')    