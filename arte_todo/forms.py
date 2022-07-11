from dataclasses import field
from django import forms
from .models import consulta,foto

class consultaForm(forms.ModelForm):
    
    class Meta:
        model = consulta
        fields = '__all__'
class fotoForm(forms.ModelForm):
    
    class Meta:
        model = foto
        fields = '__all__'
        
        widgets = {
            "fecha": forms.SelectDateWidget()
        }