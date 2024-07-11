from rest_framework import serializers
from .models import *

#Lista Estudiante
class EstudianteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = [
            'nivel',
            'nombre',
            'requisitos_cumplidos_permanecer',
            'requisitos_cumplidos_subir',
            'requisitos_cumplidos',
        ]


#Estudiante
class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = [
            'nivel',
            'nombre',
            'requisitos_cumplidos_permanecer',
            'requisitos_cumplidos_subir',
            'requisitos_cumplidos',
        ]