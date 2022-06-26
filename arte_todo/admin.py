from django.contrib import admin

from arte_todo.views import contacto
from .models import foto, contacto

# Register your models here.
admin.site.register(foto)
admin.site.register(contacto)