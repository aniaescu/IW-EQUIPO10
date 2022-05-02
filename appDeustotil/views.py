from multiprocessing import context
from django.shortcuts import  render, redirect, get_object_or_404

from appDeustotil.models import Proyecto, Tarea, Empleado, Cliente
from .forms import ProyectoForm, TareaForm, EmpleadoForm, ClienteForm
from django.views import View
from django.views.generic import ListView, DetailView

# Clase creada para visualizar la pagina principal
def index(request):
    return render(request, 'pagPrincipal.html')

# Clase creada para visualizar las tareas ordenados por fecha inicio.
class TareaListView(ListView):
    model = Tarea
    queryset = Tarea.objects.order_by('fecha_inicio')
    template_name = "tarea_list.html"

    def get_context_data(self, **kwargs):
        context = super(TareaListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Listado de Tareas'
        return context

# Clase creada para visualizar los proyectos ordenados por fecha inicio.
class ProyectoListView(ListView):
    model = Proyecto
    queryset = Proyecto.objects.order_by('fecha_inicio')
    template_name = "proyecto_list.html"

    def get_context_data(self, **kwargs):
        context = super(ProyectoListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Listado de Proyectos'
        return context

# Clase creada para visualizar los empleados ordenados por dni.
class EmpleadoListView(ListView):
    model = Empleado
    queryset = Empleado.objects.order_by('dni')
    template_name = "empleado_list.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Listado de Empleados'
        return context

# Clase creada para visualizar los clientes ordenados por nombre.
class ClienteListView(ListView):
    model = Cliente
    queryset = Cliente.objects.order_by('nombre')
    template_name = "cliente_list.html"

    def get_context_data(self, **kwargs):
        context = super(ClienteListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Listado de Clientes'
        return context


# Clase creada para visualizar la informacion de la tarea.
class TareaDetailView(DetailView):
    model = Tarea
    template_name = 'tarea.html'

    def get_context_data(self, **kwargs):
        context = super(TareaDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalle de la tarea'
        return context

# Clase creada para visualizar la informacion del proyecto.
class ProyectoDetailView(DetailView):
    model = Proyecto
    template_name = 'proyecto.html'

    def get_context_data(self, **kwargs):
        context = super(ProyectoDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalle del proyecto'
        return context   

# Clase creada para visualizar la informacion del empleado.
class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'empleado.html'

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalle del empleado'
        return context

# Clase creada para visualizar la informacion del cliente.
class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'cliente.html'

    def get_context_data(self, **kwargs):
        context = super(ClienteDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalle del cliente'
        return context


# Clase creada para añadir proyectos.
class CreateProyectoView(View):
    # Llamada para mostrar la página con el formulario de creación al usuario
    def get(self, request, *args, **kwargs):
        form = ProyectoForm()
        context = {
            'form': form,
            'titulo_pagina': 'Nuevo proyecto'
        }
        return render(request, 'proyecto_create.html', context)

    # Llamada para procesar la creación del proyecto
    def post(self, request, *args, **kwargs):
        form = ProyectoForm(request.POST)
        if form.is_valid(): 
            form.save()
            # Volvemos a la lista de proyectos
            return redirect('proyecto_list')
        # Si los datos no son válidos, mostramos el formulario nuevamente indicando los errores
        return render(request, 'proyecto_create.html', {'form': form})

# Clase creada para añadir tareas.
class CreateTareaView(View):
    # Llamada para mostrar la página con el formulario de creación al usuario
    def get(self, request, *args, **kwargs):
        form = TareaForm()
        context = {
            'form': form,
            'titulo_pagina': 'Nueva tarea'
        }
        return render(request, 'tarea_create.html', context)

    # Llamada para procesar la creación de la tarea
    def post(self, request, *args, **kwargs):
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save() 
            # Volvemos a la lista de tareas
            return redirect('tarea_list')
        # Si los datos no son válidos, mostramos el formulario nuevamente indicando los errores
        return render(request, 'tarea_create.html', {'form': form})  

# Clase creada para añadir empleados.
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
        if form.is_valid(): 
            form.save() 
            # Volvemos a la lista de empleados
            return redirect('empleado_list')
        # Si los datos no son válidos, mostramos el formulario nuevamente indicando los errores
        return render(request, 'empleado_create.html', {'form': form})  

# Clase creada para añadir clientes.
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
        if form.is_valid():
            form.save() 
            # Volvemos a la lista de clientes
            return redirect('cliente_list')
        # Si los datos no son válidos, mostramos el formulario nuevamente indicando los errores
        return render(request, 'cliente_create.html', {'form': form})  


# Clase creada para eliminar un proyecto.
def ProyectoDelete(request, pk):
#    proyect = get_object_or_404(Proyecto, id = pk)
#    proyect.delete()
    Proyecto.objects.filter(id = pk).delete()
    # Una vez el proyecto se haya eliminado, volvemos al listado de proyectos.
    return redirect('proyecto_list')

# Clase creada para eliminar una tarea.
def TareaDelete(request, pk):
#    tare = get_object_or_404(Tarea, id = pk)
#    tare.delete()
    Tarea.objects.filter(id = pk).delete()
    # Una vez la tarea se haya eliminado, volvemos al listado de tareas.
    return redirect('tarea_list')   

# Clase creada para eliminar un empleado.
def EmpleadoDelete(request, pk):
#    emplead = get_object_or_404(Tarea, id = pk)
#    emplead.delete()
    Empleado.objects.filter(id = pk).delete()
    # Una vez el empleado se haya eliminado, volvemos al listado de empleados.
    return redirect('empleado_list')   

# Clase creada para eliminar un cliente.    
def ClienteDelete(request, pk):
#    clien = get_object_or_404(Tarea, id = pk)
#    client.delete()
    Cliente.objects.filter(id = pk).delete()
    # Una vez el cliente se haya eliminado, volvemos al listado de clientes.
    return redirect('cliente_list')   

# Clase creada para modificar la informacion de una tarea.
class TareaModificar(View):
    # Llamada para mostrar la página con el formulario de creación al usuario, con la informacion de la tarea seleccionada ya en él.
    def get(self, request, pk, *args, **kwargs):
        tarea = Tarea.objects.get(id = pk)
        form = TareaForm(instance = tarea)
        context = {
            'form': form,
            'titulo_pagina': 'Modificar tarea'
        }
        return render(request, 'tarea_modificar.html', context)

    # Llamada para procesar la modificacion de la tarea.
    def post(self, request, pk,  *args, **kwargs):
        tarea = Tarea.objects.get(id = pk)
        form = TareaForm(request.POST, instance = tarea)
        if form.is_valid(): 
            form.save() 
            # Volvemos a la lista de tareas
            return redirect('tarea_list')
        # Si los datos no son válidos, mostramos el formulario nuevamente indicando los errores
        return render(request, 'tarea_modificar.html', {'form': form})  

# Clase creada para modificar la informacion de un proyecto.
class ProyectoModificar(View):
    # Llamada para mostrar la página con el formulario de creación al usuario, con la informacion del proyecto seleccionada ya en él.
    def get(self, request, pk, *args, **kwargs):
        proyecto = Proyecto.objects.get(id = pk)
        form = ProyectoForm(instance = proyecto)
        context = {
            'form': form,
            'titulo_pagina': 'Modificar proyecto'
        }
        return render(request, 'proyecto_modificar.html', context)

    # Llamada para procesar la modificacion del proyecto
    def post(self, request, pk,  *args, **kwargs):
        proyecto = Proyecto.objects.get(id = pk)
        form = ProyectoForm(request.POST, instance = proyecto)
        if form.is_valid(): 
            form.save()
            # Volvemos a la lista de proyectos
            return redirect('proyecto_list')
        # Si los datos no son válidos, mostramos el formulario nuevamente indicando los errores
        return render(request, 'proyecto_modificar.html', {'form': form})  

# Clase creada para modificar la informacion de un empleado.
class EmpleadoModificar(View):
    # Llamada para mostrar la página con el formulario de creación al usuario, con la informacion del empleado seleccionado ya en él.
    def get(self, request, pk, *args, **kwargs):
        empleado = Empleado.objects.get(id = pk)
        form = EmpleadoForm(instance = empleado)
        context = {
            'form': form,
            'titulo_pagina': 'Modificar empleado'
        }
        return render(request, 'empleado_modificar.html', context)

    # Llamada para procesar la modificacion del empleado.
    def post(self, request, pk,  *args, **kwargs):
        empleado = Empleado.objects.get(id = pk)
        form = EmpleadoForm(request.POST, instance = empleado)
        if form.is_valid():
            form.save() 
            # Volvemos a la lista de empleados
            return redirect('empleado_list')
        # Si los datos no son válidos, mostramos el formulario nuevamente indicando los errores
        return render(request, 'empleado_modificar.html', {'form': form})  

# Clase creada para modificar
class ClienteModificar(View):
    # Llamada para mostrar la página con el formulario de creación al usuario, con la informacion de la tarea seleccionada ya en él.
    def get(self, request, pk, *args, **kwargs):
        cliente = Cliente.objects.get(id = pk)
        form = ClienteForm(instance = cliente)
        context = {
            'form': form,
            'titulo_pagina': 'Modificar cliente'
        }
        return render(request, 'cliente_modificar.html', context)

    # Llamada para procesar la modificacion del cliente
    def post(self, request, pk,  *args, **kwargs):
        cliente = Cliente.objects.get(id = pk)
        form = ClienteForm(request.POST, instance = cliente)
        if form.is_valid():
            form.save() 
            # Volvemos a la lista de clientes
            return redirect('cliente_list')
        # Si los datos no son válidos, mostramos el formulario nuevamente indicando los errores
        return render(request, 'cliente_modificar.html', {'form': form})  
