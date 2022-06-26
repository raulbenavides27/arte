from django.shortcuts import render
from .models import foto
# Create your views here.
def home(request):
     return render(request,'arte_todo/home.html')

def contacto(request):
     return render(request,'arte_todo/contacto.html')
  


foto = foto.objects.all()
data = {
           'foto': foto
           }
def galeria(request):
 
   return render(request,'arte_todo/galeria.html', data)
    
def comunidad(request):
     return render(request,'arte_todo/comunidad.html')