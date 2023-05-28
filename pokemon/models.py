from django.db import models

# Create your models here.


class Datos(models.Model):
    nombre = models.CharField(max_length=40)
    numero = models.IntegerField(default=0)
    generacion = models.IntegerField(default=0)
    tipo = models.CharField(max_length=40)