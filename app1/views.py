from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return HttpResponse("<h1> Bienvenido</h1>")
def nosotros (request):
    return render(request, 'nosotros.html')
def juegos (request):
    return render(request, 'juegos/index.html')