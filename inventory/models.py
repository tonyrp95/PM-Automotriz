from django.db import models

# Create your models here.
class Autos(models.Model):
    Marca = models.CharField(max_length=200)
    Modelo = models.CharField(max_length=200)
    Kilometros = models.IntegerField()
    Año = models.IntegerField()
    Color = models.CharField(max_length=200)


class Categorias(models.Model):
    Categoria = models.CharField(max_length=200)
    Autos = models.ForeignKey(Autos, on_delete=models.CASCADE)
    
