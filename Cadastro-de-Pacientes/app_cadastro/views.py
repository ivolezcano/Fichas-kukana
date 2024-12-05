from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string

from .models import Trabajo
from .forms import TrabajoForm

from xhtml2pdf import pisa


def descargar_pdf(request, numero_trabajo):
    trabajo = get_object_or_404(Trabajo, numero_trabajo=numero_trabajo)

    template_path = 'detalle_trabajo.html'
    
    context = {'trabajo': trabajo}
    
    # Renderizar la plantilla HTML
    html = render_to_string(template_path, context)
    
    # Crear la respuesta HttpResponse con tipo de contenido PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="detalle_trabajo_{trabajo.numero_trabajo}.pdf"'

    # Convertir el HTML a PDF y guardarlo en la respuesta
    pisa_status = pisa.CreatePDF(html, dest=response)

    # Si hubo un error en la conversión, puedes manejarlo
    if pisa_status.err:
        return HttpResponse('Error al generar el PDF', status=500)

    return response

def detalle_trabajo(request, numero_trabajo):
    trabajo = get_object_or_404(Trabajo, numero_trabajo=numero_trabajo)

    return render(request, 'usuarios/detalle_trabajo.html', {'trabajo': trabajo})

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