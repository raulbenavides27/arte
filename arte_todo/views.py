from django.shortcuts import render, redirect, get_object_or_404
from .models import foto
from .forms import consultaForm , fotoForm

# Create your views here.
def home(request):
    return render(request,'arte_todo/home.html')

def respuesta(request):
    return render(request,'arte_todo/respuesta.html')

def comunidad(request):
      return render(request,'arte_todo/comunidad.html')

def galeria(request):
     fotos = foto.objects.all()
       
     data = {
          'fotos': fotos
       }

     return render(request,'arte_todo/galeria.html', data)
 
def contacto(request):
    data = { 
        'form': consultaForm
     }
    
    if request.method == 'POST':
          formulario = consultaForm(data=request.POST)
          if formulario.is_valid():
              formulario.save() 
              return redirect(to='respuesta') 
          else:
               data["form"] = formulario
 
    return render(request,'arte_todo/contacto.html', data)

def Editar(request, id):
    
      Fotos = get_object_or_404(foto, id=id)
     
      data = {
         'form': fotoForm(instance=Fotos)
      }
     
      if request.method == 'post':
          formulario = fotoForm(data=request.POST,instance=Fotos, files=request.FILES)
          if formulario.is_valid():
               formulario.save()
               data["mensaje"] = "guardado"  
          data["form"] = formulario
          data["mensaje"] = " no guardado"  
          

      return render(request,'arte_todo/editar.html', data)

def agregar(request):
    
     data = {
         'form':fotoForm
     }

     if request.method == 'POST':
          formulario = fotoForm(data=request.POST,files=request.FILES)
          if formulario.is_valid():
               formulario.save()
               return redirect(to='galeria')    
          else:
              data["form"] = formulario 
               
     return render(request,'arte_todo/agregar.html', data)



def eliminar(request, id):
    fotoss = get_object_or_404(foto, id=id)
    fotoss.delete()
    return redirect(to="galeria")


