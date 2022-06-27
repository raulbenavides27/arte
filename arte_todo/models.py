from distutils.command.upload import upload
from pyexpat import model
from turtle import update
from django.db import models

# Create your models here.
class foto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha = models.DateField()
    imagen = models.ImageField(upload_to="foto", null=True)
     
    def __str__(self):
        return self.nombre
class consulta(models.Model):
    asunto = models.CharField(max_length=50)
    correo = models.EmailField()
    contacto= models.IntegerField()
    mensaje = models.TextField()
    
    
    def __str__(self):
        return self.asunto   