from django.shortcuts import render
from .models import consulta, foto
from .forms import consultaForm

# Create your views here.
def home(request):
     return render(request,'arte_todo/home.html')

def contacto(request):
     data = { 
             'form': consultaForm
     }
     if request.method == 'POST':
          formulario = consultaForm(data=request.POST)
          if formulario.is_valid():
              formulario.save()
              data["mensaje"] = "mensaje guardado guardo"
          else:
               data["form"] = formulario
           
           
     return render(request,'arte_todo/contacto.html', data)


foto = foto.objects.all()
data = {
           'foto': foto
           }
def galeria(request):
 
   return render(request,'arte_todo/galeria.html', data)
    
def comunidad(request):
     return render(request,'arte_todo/comunidad.html')