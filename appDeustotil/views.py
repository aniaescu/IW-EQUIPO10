
from django.conf import Settings
from django.shortcuts import render, redirect, get_object_or_404
from appDeustotil.models import Proyecto, Tarea, Empleado, Cliente
from .forms import LoginForm, ProyectoForm, TareaForm, EmpleadoForm, ClienteForm
from django.views import View
from django.views.generic import ListView, DetailView
from django.db.models import Q, Case, When
from django.core.mail import send_mail
from django.conf import settings

# Clase creada para visualizar la pagina principal


def index(request):
    return render(request, 'pagPrincipal.html')

# Clase creada para visualizar las tareas ordenados por fecha inicio.
# class TareaListView(ListView):
#    model = Tarea
#    queryset = Tarea.objects.order_by('fecha_inicio')
#    template_name = "tarea_list.html"

#    def get_context_data(self, **kwargs):
#        context = super(TareaListView, self).get_context_data(**kwargs)
#        context['titulo_pagina'] = 'Listado de Tareas'
#        return context


def TareaListView(request):
    busqueda = request.GET.get("buscar")
    select = request.GET.get("select")
    tarea = Tarea.objects.all()

    if select == 'nombre':
        if busqueda:
            tarea = Tarea.objects.filter(
                Q(nombre__icontains=busqueda)
            ).distinct()
    elif select == 'prioridad':
        if busqueda:
            tarea = Tarea.objects.filter(
                Q(prioridad__icontains=busqueda)
            ).distinct()
    elif select == 'descripcion':
        if busqueda:
            tarea = Tarea.objects.filter(
                Q(descripcion__icontains=busqueda)
            ).distinct()
    elif select == 'fecha_inicio':
        if busqueda:
            tarea = Tarea.objects.filter(
                Q(fecha_inicio__icontains=busqueda)
            ).distinct()
    elif select == 'fecha_fin':
        if busqueda:
            tarea = Tarea.objects.filter(
                Q(fecha_fin__icontains=busqueda)
            ).distinct()
    elif select == 'estado':
        if busqueda:
            tarea = Tarea.objects.filter(
                Q(estado__icontains=busqueda)
            ).distinct()
    elif select == 'notas':
        if busqueda:
            tarea = Tarea.objects.filter(
                Q(notas__icontains=busqueda)
            ).distinct()

    return render(request, 'tarea_list.html', {'tarea_list': tarea})

# Clase creada para visualizar los proyectos ordenados por fecha inicio.
# class ProyectoListView(ListView):
#    model = Proyecto
#    queryset = Proyecto.objects.order_by('fecha_inicio')
#    template_name = "proyecto_list.html"

#    def get_context_data(self, **kwargs):
#         context = super(ProyectoListView, self).get_context_data(**kwargs)
#        context['titulo_pagina'] = 'Listado de Proyectos'
#        return context


def ProyectoListView(request):
    busqueda = request.GET.get("buscar")
    select = request.GET.get("select")
    proyecto = Proyecto.objects.all()

    if select == 'nombre':
        if busqueda:
            proyecto = Proyecto.objects.filter(
                Q(nombre__icontains=busqueda)
            ).distinct()
    elif select == 'presupuesto':
        if busqueda:
            proyecto = Proyecto.objects.filter(
                Q(presupuesto__icontains=busqueda)
            ).distinct()
    elif select == 'descripcion':
        if busqueda:
            proyecto = Proyecto.objects.filter(
                Q(descripcion__icontains=busqueda)
            ).distinct()
    elif select == 'fecha_inicio':
        if busqueda:
            proyecto = Proyecto.objects.filter(
                Q(fecha_inicio__icontains=busqueda)
            ).distinct()
    elif select == 'fecha_fin':
        if busqueda:
            proyecto = Proyecto.objects.filter(
                Q(fecha_fin__icontains=busqueda)
            ).distinct()

    return render(request, 'proyecto_list.html', {'proyecto_list': proyecto})

# Clase creada para visualizar los empleados ordenados por dni.
# class EmpleadoListView(ListView):
#    model = Empleado
#    queryset = Empleado.objects.order_by('dni')
#    template_name = "empleado_list.html"

#    def get_context_data(self, **kwargs):
#        context = super(EmpleadoListView, self).get_context_data(**kwargs)
#        context['titulo_pagina'] = 'Listado de Empleados'
#        return context


def EmpleadoListView(request):
    busqueda = request.GET.get("buscar")
    select = request.GET.get("select")
    empleado = Empleado.objects.all()

    if select == 'nombre':
        if busqueda:
            empleado = Empleado.objects.filter(
                Q(nombre__icontains=busqueda)
            ).distinct()
    elif select == 'dni':
        if busqueda:
            empleado = Empleado.objects.filter(
                Q(dni__icontains=busqueda)
            ).distinct()
    elif select == 'apellidos':
        if busqueda:
            empleado = Empleado.objects.filter(
                Q(apellidos__icontains=busqueda)
            ).distinct()
    elif select == 'email':
        if busqueda:
            empleado = Empleado.objects.filter(
                Q(email__icontains=busqueda)
            ).distinct()
    elif select == 'telefono':
        if busqueda:
            empleado = Empleado.objects.filter(
                Q(telefono__icontains=busqueda)
            ).distinct()

    return render(request, 'empleado_list.html', {'empleado_list': empleado})

# Clase creada para visualizar los clientes ordenados por nombre.
# class ClienteListView(ListView):
#    model = Cliente
#    queryset = Cliente.objects.order_by('nombre')
#    template_name = "cliente_list.html"

#    def get_context_data(self, **kwargs):
#        context = super(ClienteListView, self).get_context_data(**kwargs)
#        context['titulo_pagina'] = 'Listado de Clientes'
#        return context


def ClienteListView(request):
    busqueda = request.GET.get("buscar")
    select = request.GET.get("select")
    cliente = Cliente.objects.all()

    if select == 'nombre':
        if busqueda:
            cliente = Cliente.objects.filter(
                Q(nombre__icontains=busqueda)
            ).distinct()
    elif select == 'email':
        if busqueda:
            cliente = Cliente.objects.filter(
                Q(email__icontains=busqueda)
            ).distinct()
    elif select == 'telefono':
        if busqueda:
            cliente = Cliente.objects.filter(
                Q(telefono__icontains=busqueda)
            ).distinct()

    return render(request, 'cliente_list.html', {'cliente_list': cliente})

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
            empleado = Empleado()
            empleado.dni = form.cleaned_data['dni']
            empleado.nombre = form.cleaned_data['nombre']
            empleado.apellidos = form.cleaned_data['apellidos']
            empleado.email = form.cleaned_data['email']
            empleado.telefono = form.cleaned_data['telefono']
            empleado.contraseña = form.cleaned_data['contraseña']
            empleado.save()
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
            cliente = Cliente()

            cliente.nombre = form.cleaned_data['nombre']
            cliente.email = form.cleaned_data['email']
            cliente.telefono = form.cleaned_data['telefono']

            cliente.save()
            # form.save()
            # Volvemos a la lista de clientes
            return redirect('cliente_list')
        # Si los datos no son válidos, mostramos el formulario nuevamente indicando los errores
        return render(request, 'cliente_create.html', {'form': form})


# Clase creada para eliminar un proyecto.
def ProyectoDelete(request, pk):
    #    proyect = get_object_or_404(Proyecto, id = pk)
    #    proyect.delete()
    Proyecto.objects.filter(id=pk).delete()
    # Una vez el proyecto se haya eliminado, volvemos al listado de proyectos.
    return redirect('proyecto_list')

# Clase creada para eliminar una tarea.


def TareaDelete(request, pk):
    #    tare = get_object_or_404(Tarea, id = pk)
    #    tare.delete()
    Tarea.objects.filter(id=pk).delete()
    # Una vez la tarea se haya eliminado, volvemos al listado de tareas.
    return redirect('tarea_list')

# Clase creada para eliminar un empleado.


def EmpleadoDelete(request, pk):
    #    emplead = get_object_or_404(Tarea, id = pk)
    #    emplead.delete()
    Empleado.objects.filter(id=pk).delete()
    # Una vez el empleado se haya eliminado, volvemos al listado de empleados.
    return redirect('empleado_list')

# Clase creada para eliminar un cliente.


def ClienteDelete(request, pk):
    #    clien = get_object_or_404(Tarea, id = pk)
    #    client.delete()
    Cliente.objects.filter(id=pk).delete()
    # Una vez el cliente se haya eliminado, volvemos al listado de clientes.
    return redirect('cliente_list')

# Clase creada para modificar la informacion de una tarea.


class TareaModificar(View):
    # Llamada para mostrar la página con el formulario de creación al usuario, con la informacion de la tarea seleccionada ya en él.
    def get(self, request, pk, *args, **kwargs):
        tarea = Tarea.objects.get(id=pk)
        form = TareaForm(instance=tarea)
        context = {
            'form': form,
            'titulo_pagina': 'Modificar tarea'
        }
        return render(request, 'tarea_modificar.html', context)

    # Llamada para procesar la modificacion de la tarea.
    def post(self, request, pk,  *args, **kwargs):
        tarea = Tarea.objects.get(id=pk)
        form = TareaForm(request.POST, instance=tarea)
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
        proyecto = Proyecto.objects.get(id=pk)
        form = ProyectoForm(instance=proyecto)
        context = {
            'form': form,
            'titulo_pagina': 'Modificar proyecto'
        }
        return render(request, 'proyecto_modificar.html', context)

    # Llamada para procesar la modificacion del proyecto
    def post(self, request, pk,  *args, **kwargs):
        proyecto = Proyecto.objects.get(id=pk)
        form = ProyectoForm(request.POST, instance=proyecto)
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
        empleado = Empleado.objects.get(id=pk)
        form = EmpleadoForm(instance=empleado)
        context = {
            'form': form,
            'titulo_pagina': 'Modificar empleado'
        }
        return render(request, 'empleado_modificar.html', context)

    # Llamada para procesar la modificacion del empleado.
    def post(self, request, pk,  *args, **kwargs):
        empleado = Empleado.objects.get(id=pk)
        form = EmpleadoForm(request.POST, instance=empleado)
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
        cliente = Cliente.objects.get(id=pk)
        form = ClienteForm(instance=cliente)
        context = {
            'form': form,
            'titulo_pagina': 'Modificar cliente'
        }
        return render(request, 'cliente_modificar.html', context)

    # Llamada para procesar la modificacion del cliente
    def post(self, request, pk,  *args, **kwargs):
        cliente = Cliente.objects.get(id=pk)
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            # Volvemos a la lista de clientes
            return redirect('cliente_list')
        # Si los datos no son válidos, mostramos el formulario nuevamente indicando los errores
        return render(request, 'cliente_modificar.html', {'form': form})

# Llamada para mostrar el formulario de login.


def loginform(request):
    form = LoginForm()
    return render(request, 'login.html', {'form': form})

# Función para autenticar empleados (usuarios)


def login(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        nombre = form.cleaned_data['nombre']
        contraseña = form.cleaned_data['contraseña']

        usuarios = Empleado.objects.order_by('nombre')
        valido = False

        # Comparación de nombre y contraseña insertadas por el usuario con los empleados almacenados en la base de datos
        for u in usuarios:
            if u.nombre == nombre and u.contraseña == contraseña:
                valido = True

        if valido == True:
            # Redirigimos al usuario hacia la página principal de la página web
            return redirect('pagPrincipal')
        else:
            # Si el usuario o la contraseña no son los correctos, volvemos a mostrar el formulario de login
            return render(request, 'login.html', {'form': form})
    else:
        # Si el usuario o la contraseña no son los correctos, volvemos a mostrar el formulario de login
        return render(request, 'login.html', {'form': form})


def ContactoView(request):

    if request.method == "POST":

        subject = request.POST["asunto"]
        message = request.POST["mensaje"] + " " + request.POST["email"]
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ["deustotil@gmail.com"]
        send_mail(subject, message,email_from, recipient_list)

        return render(request, "gracias.html")
    
    return render(request, "contacto.html")
