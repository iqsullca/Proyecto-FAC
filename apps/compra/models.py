from django.db import models

# Create your models here.

class Proveedor(models.Model):
	codigo = models.CharField(max_length=12)
	nombre = models.CharField(max_length=100)
	apeparterno = models.CharField(max_length=50)
	apemarterno = models.CharField(max_length=50)
	numerodocumento = models.CharField(max_length=20)
	web = models.CharField(max_length=100)
	razonsocial = models.CharField(max_length=120)
	email = models.EmailField()
	telefono = models.CharField(max_length=12)
	celular = models.CharField(max_length=12)
	direccion = models.TextField()

	def __str__(self):
		return '{} {}'.format(self.nombre, self.apeparterno)

