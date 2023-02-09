from django.db import models

class Producto(models.Model):
    codigo_producto = models.IntegerField()
    nombre_producto = models.CharField(max_length=20, default="nombre_producto")
    precio = models.FloatField()
    stock = models.IntegerField(default=6)
    num_comprados = models.IntegerField()

    