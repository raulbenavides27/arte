from distutils.command.upload import upload
from pyexpat import model
from turtle import update
from django.db import models

# Create your models here.
class foto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha = models.DateField()
    imagen = models.ImageField(upload_to="foto")
     
    def __str__(self):
        return self.nombre
    
    
opciones_asunto=[
        [0,"consulta"],
        [1,"reclamo"],
        [2,"sugerencia"],
]
class consulta(models.Model):
    nombre = models.CharField(max_length=50)
    asunto = models.IntegerField(choices=opciones_asunto)
    correo = models.EmailField()
    contacto= models.IntegerField()
    mensaje = models.TextField()
    
    
    def __str__(self):
        return self.asunto   