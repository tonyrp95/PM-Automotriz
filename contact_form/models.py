from django.db import models

# Create your models here.
class Contacto(models.Model):
    Nombres = models.CharField(max_length=200, blank= False, null= False)
    Apellidos = models.CharField(max_length=200, blank= False, null= False)
    Correo = models.EmailField(blank= False, null= False)
    Telefono = models.IntegerField(blank= False, null= False)
    Mensaje = models.TextField(max_length=200, blank= False, null= False)


