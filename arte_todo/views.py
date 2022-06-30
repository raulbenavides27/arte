from django.shortcuts import render
from .models import consulta, foto
from .forms import consultaForm , fotoForm

# Create your views here.
def home(request):
     return render(request,'arte_todo/home.html')

def respuesta(request):
     
      return render(request,'arte_todo/respuesta.html')
 
def contacto(request):
     
     data = { 
             'form': consultaForm
     }
     if request.method == 'POST':
          formulario = consultaForm(data=request.POST)
          if formulario.is_valid():
              formulario.save() 
              return render(request,'arte_todo/respuesta.html') 
          else:
               data["form"] = formulario
               data["mensaje"] = "mensaje sin enviar"
           
     return render(request,'arte_todo/contacto.html', data)


foto = foto.objects.all()
data = {
           'foto': foto
           }
def galeria(request):
 
   return render(request,'arte_todo/galeria.html', data)

def agregar(request):
     data = {
         'form':fotoForm
     }
     
     if request.method == 'POST':
          formulario = fotoForm(data=request.POST,files=request.FILES)
          if formulario.is_valid():
               formulario.save()
               return render(request,'arte_todo/respuesta.html')    
          else:
           data["form"] = formulario 
               
     return render(request,'arte_todo/agregar.html', data)

    
def comunidad(request):
     return render(request,'arte_todo/comunidad.html')

def editar(request):
      return render(request,'arte_todo/editar.html')
 
def eliminar(request):
      return render(request,'arte_todo/eliminar.html')

