from django.shortcuts import render, redirect, get_object_or_404
from .models import foto
from .forms import consultaForm ,fotoForm, customUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login

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
           
              messages.success(request, "Mensaje Enviado")
              return redirect(to='contacto') 
          else:
               data["form"] = formulario
 
    return render(request,'arte_todo/contacto.html', data)

def agregar(request):
     data = {
         'form':fotoForm
     }

     if request.method == 'POST':
          formulario = fotoForm(data=request.POST,files=request.FILES)
          if formulario.is_valid():
               formulario.save()
               messages.success(request, "Foto Agregada")
               return redirect(to='galeria')    
          else:
              data["form"] = formulario 
               
     return render(request,'arte_todo/agregar.html', data)

def editar(request, id):
    
      Fotos = get_object_or_404(foto, id=id)
     
      data = {
         'form': fotoForm(instance=Fotos)
      }
      if request.method == 'POST':
          formulario = fotoForm(data=request.POST,instance=Fotos, files=request.FILES)
          if formulario.is_valid():
               formulario.save()
               messages.success(request, "Foto editada")
               return redirect(to='galeria')  
          data["form"] = formulario
      return render(request,'arte_todo/editar.html', data)
  
def eliminar(request, id):
    fotoss = get_object_or_404(foto, id=id)
    fotoss.delete()
    messages.success(request, "Foto eliminada")
    return redirect(to="galeria")

def registro(request):
    data = {
        'form': customUserCreationForm()
    }
    if request.method == 'POST':
       formulario = customUserCreationForm(data=request.POST)
       if formulario.is_valid():
          formulario.save()
          user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"]) 
          login(request, user)
          messages.success(request, "Usuario Registrado")
          return redirect(to='home') 
       data["form"]= formulario 
       
    return render(request, 'registration/registro.html', data)


