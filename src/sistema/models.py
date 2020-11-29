from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre=models.CharField(max_length=25)
    rut=models.CharField(max_length=10)
    email=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    telefono=models.IntegerField()


    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    articulo=models.CharField(max_length=25)
    descripcion=models.CharField(max_length=50)
    precio=models.IntegerField()
    cliente=models.ForeignKey(Cliente, on_delete=models.CASCADE)


    def __str__(self):
        return self.articulo