from django.shortcuts import render, redirect
from .models import Meteria

# Create your views here.

def agregar_materia(request):
    if request.method == 'POST':
        nombre = request.POST.get("nombre")
        comentario = request.POST.get("comentario")

        if nombre and comentario:
            Meteria.objects.create(nombre=nombre, comentario=comentario)
        return redirect("agregar")
    
    materias = Meteria.objects.all().order_by('-fecha')
    
    return render(request, "agregar.html", {"materias": materias})
