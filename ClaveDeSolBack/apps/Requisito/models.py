from django.db import models


class Requisito(models.Model):
    id = models.IntegerField
    nombre = models.CharField(max_length=80)
    permanecer = models.BooleanField()
    subir = models.BooleanField()

    

    def __str__(self):
        return self.nombre
