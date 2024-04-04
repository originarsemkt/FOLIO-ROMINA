from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')
def proyectos(request):
    return render(request, 'pages/proyectos.html')
def informacion_personal(request):
    return render(request, 'pages/informacion_personal.html')
def contacto(request):
    return render(request, 'pages/contacto.html')
def habilidades(request):
    return render(request, 'pages/habilidades.html')