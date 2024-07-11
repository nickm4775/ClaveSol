from django.db import models
from apps.User.models import *
from apps.Requisito.models import *


class Nivel(models.Model):
    id= models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    requisitos = models.ManyToManyField(Requisito, related_name='requisitos_nivel', blank = True)

    def __str__(self):
        return self.nombre
