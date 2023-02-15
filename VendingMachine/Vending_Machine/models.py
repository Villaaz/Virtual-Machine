from django.db import models
from django.urls import reverse

class Producto(models.Model):
    codigo_producto = models.IntegerField()
    nombre_producto = models.CharField(max_length=20, default="nombre_producto")
    precio = models.FloatField()
    stock = models.IntegerField(default=6)
    num_comprados = models.IntegerField(default=0)

    def get_edit_url(self):
        return reverse('edit-producto', args=[str(self.id)])
