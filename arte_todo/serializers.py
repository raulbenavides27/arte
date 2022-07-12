from .models import foto 
from rest_framework import serializers

class fotoSerializer(serializers.ModelSerializer):
    
    def validate_nombre(self, value):
        
        existe = foto.objects.filter(nombre=value).exists()
        if existe:
            raise serializers.ValidationError("este nombre ya esta uso")
        return value
    class Meta:
        model = foto
        fields = '__all__'
       # field = ('nombre','descripcion','fecha','imagen')
