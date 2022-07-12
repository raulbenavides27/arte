from django.contrib import admin

from arte_todo.views import contacto
from .models import foto, consulta

# Register your models here.

class ProductoAdmin (admin.ModelAdmin):
    

admin.site.register(foto)
admin.site.register(consulta, ProductoAdmin)