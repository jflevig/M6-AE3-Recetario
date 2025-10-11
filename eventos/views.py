from django.shortcuts import render, redirect
from .models import Evento
from django.contrib.auth import logout
from django.views.generic import View, TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from eventos.formularios import FormularioEvento 


eventos_registrados = [] 

def eventos(request): #vista basada en funciones, del M6aE4    
    if request.method == 'POST':
        formulario = FormularioEvento(request.POST)
        if formulario.is_valid():
            evento_data = {
                'nombre_evento': formulario.cleaned_data['nombre_evento'],
                'fecha_evento': formulario.cleaned_data['fecha_evento'],
                'ubicacion': formulario.cleaned_data['ubicacion'],
                'autor_evento': request.user.username
            }

            eventos_registrados.append(evento_data)
            print("--- Nuevo Evento Registrado (en lista) ---")
            print(evento_data)
            return redirect('evento_exito')
        else:
            return render(request, 'eventos.html', {'formulario': formulario})
    else:
        formulario = FormularioEvento()
        return render(request, 'eventos.html', {'formulario': formulario})

def evento_exito(request):
    return render(request, 'evento_exito.html')

def lista_eventos(request): # basada en funciones
    contexto = {'eventos': eventos_registrados}
    return render(request, 'lista_eventos.html', contexto)


#class EditarEvento(PermissionRequiredMixin, TemplateView):

#class EliminarEvento

class PaginaProhibida(TemplateView):
    template_name = "pagina_prohibida.html"