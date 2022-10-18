from django.shortcuts import render
from .models import Certificados
# Create your views here.

def certificados(request):
    certificado = Certificados.objects.all()
    return render(request, "certificados/certificados.html", {'certificado':certificado})