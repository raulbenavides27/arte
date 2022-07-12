from dataclasses import field
from pyexpat import model
from django import forms
from .models import consulta,foto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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
        
class customUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email", "password1", "password2"]