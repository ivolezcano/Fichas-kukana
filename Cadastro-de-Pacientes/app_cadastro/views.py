from django.shortcuts import render

from .models import Usuario
from .forms import UsuarioForm

def home(request):
    return render(request,'usuarios/home.html')


def usuarios(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'usuarios/form.html', {'form': form})

    usuarios = {'usuarios': Usuario.objects.all()}
    return render(request, 'usuarios/usuarios.html', usuarios)