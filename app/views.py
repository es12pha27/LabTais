from django.shortcuts import render
from django.http import HttpResponse
from .models import Taller
#Encontrar el template para mostrarle al usuario

def home(request):
    return render(request,'app/home.html')

def lista(request):
    talleres=Taller.objects.all()
    return HttpResponse(talleres)

def galeria(request):
    return render(request,'app/galeria.html')

def contacto(request):
    return render(request,'app/contacto.html')