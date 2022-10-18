from django.shortcuts import render
from .models import Proyectos
# Create your views here.

def proyectos(request):
    proyecto = Proyectos.objects.all()
    return render(request, "proyectos/proyectos.html", {'proyecto':proyecto})