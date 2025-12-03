from django.db import models

# Create your models here.
class Estado(models.Model):
    nombre=models.CharField(max_length=100, unique=True)
    clave=models.CharField(max_length=3, unique=True)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.clave + '-' + self.nombre
class municipio(models.Model):
    nombre=models.CharField(max_length=100, unique=True)
    estadop=models.ForeignKey(Estado, on_delete=models.CASCADE, related_name='municipios')
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.estadop} - {self.nombre}"
class colonia(models.Model):
    nombre=models.CharField(max_length=100, unique=True)
    municipio_p=models.ForeignKey(municipio, on_delete=models.CASCADE, related_name='colonias')
    codigo_p = models.CharField(max_length=6,)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.nombre} - {self.municipio_p}"
    
