from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.nombre
    
class atencion(models.Model):
    veterinaria = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    descripcion = models.TextField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"{self.veterinaria.nombre} - {self.fecha} {self.hora}"
