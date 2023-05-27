from django.db import models

# Create your models here.


class Datos(models.Model):
    nombre = models.CharField(max_length=40)
    numero = models.IntegerField
    generacion = models.IntegerField
    tipo = models.CharField(max_length=40)