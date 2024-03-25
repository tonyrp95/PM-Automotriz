from django.db import models

# Create your models here.
class Registro(models.Model):
    Nombres = models.CharField(max_length=200, blank= False, null= False)
    Apellidos = models.CharField(max_length=200, blank= False, null= False)
    Correo = models.EmailField(blank= False, null= False)
    Nombre_Usuario = models.CharField(max_length= 15, blank= False, null= False)
    Contraseña = models.CharField(max_length= 15, blank= False, null= False)
    
