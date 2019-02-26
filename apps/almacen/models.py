from django.db import models

# Create your models here.
from apps.compra.models import Proveedor


class Producto(models.Model):
	codigo = models.CharField(max_length=20)
	nombre = models.CharField(max_length=100)
	preciocosto = models.DecimalField(max_digits=10,decimal_places=8)
	precioventa = models.DecimalField(max_digits=10,decimal_places=8)
	cantidad = models.IntegerField()
	stock = models.IntegerField()
	stockminimo = models.IntegerField()
	proveedor = models.ForeignKey(Proveedor,null=True, blank=True,on_delete=models.CASCADE)

	def __str__(self):
		return '{}'.format(self.nombre)


	