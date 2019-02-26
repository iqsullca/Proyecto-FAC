from django.db import models

# Create your models here.
from apps.almacen.models import Producto
class Cliente(models.Model):
	numerodocumento = models.CharField(max_length=20)
	nombre = models.CharField(max_length=100)
	apeparterno = models.CharField(max_length=50)
	apemarterno = models.CharField(max_length=50)
	sexo = models.CharField(max_length=10)
	fechanacimiento = models.DateField()
	fecharegistro = models.DateField()
	email = models.EmailField()
	telefono = models.CharField(max_length=12)
	celular = models.CharField(max_length=12)
	direccion = models.TextField()

	def __str__(self):
		return '{} {}'.format(self.nombre, self.apemarterno)


class Venta(models.Model):
	descripcion = models.CharField(max_length = 100)
	monto = models.DecimalField(max_digits=10,decimal_places=8)
	pendiente = models.DecimalField(max_digits=10,decimal_places=8)
	fecha = models.DateField()
	fechavencimiento = models.DateField()
	tipocambio = models.DecimalField(max_digits=10,decimal_places=8)
	cliente = models.ForeignKey(Cliente,null=True,blank=True,on_delete=models.CASCADE)
	producto = models.ManyToManyField(Producto,blank=True)
