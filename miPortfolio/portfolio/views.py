
from django.shortcuts import HttpResponse, render
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
# Create your views here.

def home(request):
    return render(request, "portfolio/pages/sobreMi.html")

def certificados(request):
    return render(request, "portfolio/pages/certificados.html")

def contacto(request):
    return render(request, "portfolio/pages/contacto.html")

def sobreMi(request):
    return render(request, "portfolio/pages/sobreMi.html")

def sobreMi(request):
    return render(request, "portfolio/pages/sobreMi.html")
