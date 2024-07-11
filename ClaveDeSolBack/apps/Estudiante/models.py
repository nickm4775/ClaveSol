from django.db import models
from apps.Requisito.models import *
from apps.Nivel.models import *
from apps.User.models import *

class Estudiante(models.Model):
    # Relación con el modelo Nivel
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)
    # Relación con el modelo Usuario
    nombre = models.ForeignKey(UserAccount, on_delete=models.CASCADE)

    requisitos_cumplidos = models.ManyToManyField(Requisito, related_name='estudiantes_cumplieron', blank = True)
    # Conjunto de requisitos cumplidos necesarios para permanecer en el nivel
    requisitos_cumplidos_permanecer = models.ManyToManyField(Requisito, related_name='estudiantes_cumplieron_permanecer', blank = True)
    # Conjunto de requisitos cumplidos necesarios para subir de nivel
    requisitos_cumplidos_subir = models.ManyToManyField(Requisito, related_name='estudiantes_cumplieron_subir', blank = True)

    # Método para verificar si el estudiante cumple los requisitos necesarios para permanecer en el nivel actual
    def cumple_requisitos_permanecer(self):
        # Obtiene los requisitos necesarios para permanecer en el nivel actual
        requisitos_necesarios_permanecer = self.nivel.requisitos.filter(permanecer=True)
        # Verifica si el conjunto de requisitos cumplidos es igual al conjunto de requisitos necesarios para permanecer
        return set(requisitos_necesarios_permanecer) == set(self.requisitos_cumplidos_permanecer.all())

    # Método para verificar si el estudiante cumple los requisitos necesarios para subir de nivel
    def cumple_requisitos_subir(self):
        # Obtiene los requisitos necesarios para subir de nivel
        requisitos_necesarios_subir = self.nivel.requisitos.filter(subir=True)
        # Verifica si el conjunto de requisitos cumplidos es igual al conjunto de requisitos necesarios para subir
        return set(requisitos_necesarios_subir) == set(self.requisitos_cumplidos_subir.all())

