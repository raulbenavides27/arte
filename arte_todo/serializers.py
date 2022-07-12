from .models import foto 
from rest_framework import serializers

class fotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = foto
        fields = '__all__'
       # field = ('nombre','descripcion','fecha','imagen')
