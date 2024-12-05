from django.shortcuts import render

from .models import Trabajo
from .forms import TrabajoForm

def home(request):
    if request.method == "POST":
        form = TrabajoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'usuarios/home.html', {'form': TrabajoForm(), 'message': 'Ficha registrada exitosamente!'})
        else:
            return render(request, 'usuarios/home.html', {'form': form})
    else:
        form = TrabajoForm()  # Crear un formulario vacío para mostrar en el inicio
    return render(request, 'usuarios/home.html', {'form': form})


def trabajos(request):
    if request.method == "POST":
        form = TrabajoForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirigir a la lista de trabajos después de guardar
            return render(request, 'usuarios/fichas.html', {'trabajos': Trabajo.objects.all()})
        else:
            # Si el formulario no es válido, muestra el formulario en la misma página
            return render(request, 'usuarios/fichas.html', {'form': form, 'trabajos': Trabajo.objects.all()})


    trabajos = {'trabajos': Trabajo.objects.all()}
    return render(request, 'usuarios/fichas.html', trabajos)