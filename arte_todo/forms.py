from dataclasses import field
from django import forms
from .models import consulta

class consultaForm(forms.ModelForm):
    
    class Meta:
        model = consulta
        #fields = ("asunto","correo", "contacto","mensaje")
        fields = '__all__'