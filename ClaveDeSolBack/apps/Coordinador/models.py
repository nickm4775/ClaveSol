from django.db import models
from apps.User.models import *
from apps.Nivel.models import *

# Create your models here.
class Coordinador(models.Model):
    nombre = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)