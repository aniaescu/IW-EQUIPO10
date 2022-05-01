from multiprocessing import context
from django.shortcuts import  render, redirect, get_object_or_404

from appDeustotil.models import Proyecto, Tarea, Empleado, Cliente
from .forms import ProyectoForm, TareaForm, EmpleadoForm, ClienteForm
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

class TareaModificar(View):
    # Llamada para mostrar la página con el formulario de creación al usuario
    def get(self, request, pk, *args, **kwargs):
        tarea = Tarea.objects.get(id = pk)
        form = TareaForm(instance = tarea)
        context = {
            'form': form,
            'titulo_pagina': 'Modificar tarea'
        }
        return render(request, 'tarea_modificar.html', context)

    # Llamada para procesar la creación de la noticia
    def post(self, request, pk,  *args, **kwargs):
        tarea = Tarea.objects.get(id = pk)
        form = TareaForm(request.POST, instance = tarea)
        if form.is_valid(): # is_valid() deja los datos validados en el atributo cleaned_data
            

            form.save() # Abreviación de lo anterior

            # Volvemos a la lista de noticias
            return redirect('tarea_list')
        # Si los datos no son válidos, mostramos el formulario nuevamente indicando los errores
        return render(request, 'tarea_modificar.html', {'form': form})  


class ProyectoModificar(View):
    # Llamada para mostrar la página con el formulario de creación al usuario
    def get(self, request, pk, *args, **kwargs):
        proyecto = Proyecto.objects.get(id = pk)
        form = ProyectoForm(instance = proyecto)
        context = {
            'form': form,
            'titulo_pagina': 'Modificar proyecto'
        }
        return render(request, 'proyecto_modificar.html', context)

    # Llamada para procesar la creación de la noticia
    def post(self, request, pk,  *args, **kwargs):
        proyecto = Proyecto.objects.get(id = pk)
        form = ProyectoForm(request.POST, instance = proyecto)
        if form.is_valid(): # is_valid() deja los datos validados en el atributo cleaned_data
            

            form.save() # Abreviación de lo anterior

            # Volvemos a la lista de noticias
            return redirect('proyecto_list')
        # Si los datos no son válidos, mostramos el formulario nuevamente indicando los errores
        return render(request, 'proyecto_modificar.html', {'form': form})  

class EmpleadoListView(ListView):
    model = Empleado
    queryset = Empleado.objects.order_by('dni')
    template_name = "empleado_list.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Listado de Empleados'
        return context

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'empleado.html'

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalle del empleado'
        return context

class CreateEmpleadoView(View):
    # Llamada para mostrar la página con el formulario de creación al usuario
    def get(self, request, *args, **kwargs):
        form = EmpleadoForm()
        context = {
            'form': form,
            'titulo_pagina': 'Nuevo empleado'
        }
        return render(request, 'empleado_create.html', context)

    # Llamada para procesar la creación del empleado
    def post(self, request, *args, **kwargs):
        form = EmpleadoForm(request.POST)
        if form.is_valid(): # is_valid() deja los datos validados en el atributo cleaned_data
            

            form.save() # Abreviación de lo anterior

            # Volvemos a la lista de noticias
            return redirect('empleado_list')
        # Si los datos no son válidos, mostramos el formulario nuevamente indicando los errores
        return render(request, 'empleado_create.html', {'form': form})  

def EmpleadoDelete(request, pk):
#    tare = get_object_or_404(Tarea, id = pk)
#    tare.delete()
    Empleado.objects.filter(id = pk).delete()

    return redirect('empleado_list')   

class EmpleadoModificar(View):
    # Llamada para mostrar la página con el formulario de creación al usuario
    def get(self, request, pk, *args, **kwargs):
        empleado = Empleado.objects.get(id = pk)
        form = EmpleadoForm(instance = empleado)
        context = {
            'form': form,
            'titulo_pagina': 'Modificar empleado'
        }
        return render(request, 'empleado_modificar.html', context)

    # Llamada para procesar la creación de la noticia
    def post(self, request, pk,  *args, **kwargs):
        empleado = Empleado.objects.get(id = pk)
        form = EmpleadoForm(request.POST, instance = empleado)
        if form.is_valid(): # is_valid() deja los datos validados en el atributo cleaned_data
            

            form.save() # Abreviación de lo anterior

            # Volvemos a la lista de noticias
            return redirect('empleado_list')
        # Si los datos no son válidos, mostramos el formulario nuevamente indicando los errores
        return render(request, 'empleado_modificar.html', {'form': form})  

class ClienteListView(ListView):
    model = Cliente
    queryset = Cliente.objects.order_by('nombre')
    template_name = "cliente_list.html"

    def get_context_data(self, **kwargs):
        context = super(ClienteListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Listado de Clientes'
        return context

class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'cliente.html'

    def get_context_data(self, **kwargs):
        context = super(ClienteDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalle del cliente'
        return context

class CreateClienteView(View):
    # Llamada para mostrar la página con el formulario de creación al usuario
    def get(self, request, *args, **kwargs):
        form = ClienteForm()
        context = {
            'form': form,
            'titulo_pagina': 'Nuevo cliente'
        }
        return render(request, 'cliente_create.html', context)

    # Llamada para procesar la creación del cliente
    def post(self, request, *args, **kwargs):
        form = ClienteForm(request.POST)
        if form.is_valid(): # is_valid() deja los datos validados en el atributo cleaned_data
            

            form.save() # Abreviación de lo anterior

            # Volvemos a la lista de noticias
            return redirect('cliente_list')
        # Si los datos no son válidos, mostramos el formulario nuevamente indicando los errores
        return render(request, 'cliente_create.html', {'form': form})  

def ClienteDelete(request, pk):
#    tare = get_object_or_404(Tarea, id = pk)
#    tare.delete()
    Cliente.objects.filter(id = pk).delete()

    return redirect('cliente_list')   

class ClienteModificar(View):
    # Llamada para mostrar la página con el formulario de creación al usuario
    def get(self, request, pk, *args, **kwargs):
        cliente = Cliente.objects.get(id = pk)
        form = ClienteForm(instance = cliente)
        context = {
            'form': form,
            'titulo_pagina': 'Modificar cliente'
        }
        return render(request, 'cliente_modificar.html', context)

    # Llamada para procesar la creación del cliente
    def post(self, request, pk,  *args, **kwargs):
        cliente = Cliente.objects.get(id = pk)
        form = ClienteForm(request.POST, instance = cliente)
        if form.is_valid(): # is_valid() deja los datos validados en el atributo cleaned_data
            

            form.save() # Abreviación de lo anterior

            # Volvemos a la lista de noticias
            return redirect('cliente_list')
        # Si los datos no son válidos, mostramos el formulario nuevamente indicando los errores
        return render(request, 'cliente_modificar.html', {'form': form})  
