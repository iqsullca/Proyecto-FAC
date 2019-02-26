from django import forms
from apps.venta.models import Cliente

class ClienteForm(forms.ModelForm):

  class Meta:
  	model = Cliente

  	fields = [
  	    'numerodocumento',
		'nombre',
		'apeparterno',
		'apemarterno',
		'sexo',
		'fechanacimiento',
		'fecharegistro',
		'email',
		'telefono',
		'celular', 
		'direccion',
  	]
  	labels = {
  		'numerodocumento': 'Numero',
		'nombre': 'Nombre',
		'apeparterno': 'Apellido Paterno',
		'apemarterno': 'Apellido Materno',
		'sexo': 'Sexo',
		'fechanacimiento': 'Fecha Nacimiento',
		'fecharegistro': 'Fecha Registro',
		'email': 'Email',
		'telefono': 'Teléfono',
		'celular': 'Celular', 
		'direccion': 'Dirección',
  	}
  	widgets = {
  		'numerodocumento': forms.TextInput(attrs={'class':'form-control'}),
		'nombre': forms.TextInput(attrs={'class':'form-control'}),
		'apeparterno': forms.TextInput(attrs={'class':'form-control'}),
		'apemarterno': forms.TextInput(attrs={'class':'form-control'}),
		'sexo': forms.TextInput(attrs={'class':'form-control'}),
		'fechanacimiento': forms.TextInput(attrs={'class':'form-control'}),
		'fecharegistro': forms.TextInput(attrs={'class':'form-control'}),
		'email': forms.TextInput(attrs={'class':'form-control'}),
		'telefono': forms.TextInput(attrs={'class':'form-control'}),
		'celular': forms.TextInput(attrs={'class':'form-control'}),
		'direccion': forms.TextInput(attrs={'class':'form-control'}),
  	}

