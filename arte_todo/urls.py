from django.urls import path, include
from .views import home, contacto, galeria, comunidad, agregar, respuesta, editar, eliminar, registro, fotoViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('foto',fotoViewset)


urlpatterns = [
    path('',home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('galeria/', galeria, name="galeria"),
    path('comunidad/', comunidad, name="comunidad"),
    path('agregar/', agregar, name="agregar"),
    path('respuesta/', respuesta, name="respuesta"),
    path('editar/<id>/', editar, name="editar"),
    path('eliminar/<id>/', eliminar, name="eliminar"),
    path('registro/', registro, name="registro"),
    path ('api/',include(router.urls)),
]
