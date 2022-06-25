from django.shortcuts import render

# Create your views here.
def home(request):
     return render(request,'arte_todo/home.html')

def contacto(request):
     return render(request,'arte_todo/contacto.html')

def galeria(request):
     return render(request,'arte_todo/galeria.html')

def comunidad(request):
     return render(request,'arte_todo/comunidad.html')