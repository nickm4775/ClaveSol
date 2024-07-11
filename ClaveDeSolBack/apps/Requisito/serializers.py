from rest_framework import serializers
from .models import *

#Lista requisito
class RequisitoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requisito
        fields = [
            'id',
            'nombre',
            'permanecer',
            'subir',
        ]


#Requisito
class RequisitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requisito
        fields = [
            'id',
            'nombre',
            'permanecer',
            'subir',
        ]