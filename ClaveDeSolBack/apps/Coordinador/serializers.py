from rest_framework import serializers
from .models import *

#Lista Coordinador
class CoordinadorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinador
        fields = [
            'nombre',
            'nivel',
            
        ]


#Coordinador
class CoordinadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinador
        fields = [
            'nombre',
            'nivel',
        ]