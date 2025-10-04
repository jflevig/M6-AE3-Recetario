from django.shortcuts import render, redirect
from eventos.formularios import FormularioEvento

# Create your views here.

eventos_registrados = []

def eventos(request):
    if request.method == 'POST':
        formulario = FormularioEvento(request.POST)
        if formulario.is_valid():
            nombre_evento = formulario.cleaned_data['nombre_evento']
            fecha_evento = formulario.cleaned_data['fecha_evento']
            ubicacion = formulario.cleaned_data['ubicacion']
            evento_data = {
                'nombre_evento': nombre_evento,
                'fecha_evento': fecha_evento,
                'ubicacion': ubicacion
            }
            eventos_registrados.append(evento_data)
            print(eventos_registrados)
            return redirect('evento_exito')
        else:
            return render(request, 'eventos.html', {'formulario': formulario})
    else:
        formulario = FormularioEvento()
        return render(request, 'eventos.html', {'formulario': formulario, 'eventos': eventos_registrados})
    
def evento_exito(request):
    return render(request, 'evento_exito.html')