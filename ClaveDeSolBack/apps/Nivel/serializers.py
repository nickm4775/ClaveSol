from rest_framework import serializers
from .models import *

#Lista Nivel
class NivelListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Nivel
        fields = [
            'id',
            'nombre',
            'requisitos',
        ]


#Nivel
class NivelSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = Nivel
        fields = [
            'id',
            'nombre',
            'requisitos',
        ]