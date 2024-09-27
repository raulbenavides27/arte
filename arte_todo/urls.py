
from django.urls import path
from .views import home, contacto, galeria, comunidad, agregar, respuesta, Editar, eliminar
urlpatterns = [
    path('',home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('galeria/', galeria, name="galeria"),
    path('comunidad/', comunidad, name="comunidad"),
    path('agregar/', agregar, name="agregar"),
    path('respuesta/', respuesta, name="respuesta"),
    path('editar/<id>/', Editar, name="editar"),
    path('eliminar/<id>/', eliminar, name="eliminar"),
    

]
