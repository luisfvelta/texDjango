from django.db import models

class Cliente (models.Model):
	fecha_creacion = models.DateTimeField (auto_now_add = True)
	rut = models.CharField (max_length = 14)
	descripcion = models.CharField (max_length = 100)	
	email = models.CharField (max_length = 100)
	telefono = models.CharField (max_length = 15)
	direccion = models.CharField (max_length = 100)
	comuna = models.CharField (max_length = 30)
	ciudad = models.CharField (max_length = 30)
	region = models.CharField (max_length = 50)
	codigo_postal = models.CharField (max_length = 20)

	def __str__(self):
		return(f"{self.rut} {self.descripcion}")

	class Meta:
		db_table = "clientes"


class Producto (models.Model):
	fecha_creacion = models.DateTimeField (auto_now_add = True)
	familia = models.CharField (max_length = 14)
	descripcion = models.CharField (max_length = 60)	
	marca = models.CharField (max_length = 20)
	proveedor = models.CharField (max_length = 20)
	unidad_medida = models.CharField (max_length = 5)
	peso_en_gramos = models.IntegerField	
	costo_unitario = models.DecimalField
	precio_detal = models.DecimalField
	precio_canal = models.DecimalField
	precio_fabricante = models.DecimalField
	precio_lista = models.DecimalField
	precio_corporativo = models.DecimalField
	existencias = models.IntegerField	


	def __str__(self):
		return(f"{self.familia} {self.marca} {self.descripcion}")

	class Meta:
		db_table = "productos"

