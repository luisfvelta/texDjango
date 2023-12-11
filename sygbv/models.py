from django.db import models

class Documento (models.Model):
	pFecha = models.DateField ()
	pDocumento = models.CharField(max_length = 10)
	pControl = models.CharField(max_length = 10)
	pCliente = models.CharField (max_length = 50)	
	pRIF = models.CharField (max_length = 15)
	pProducto = models.CharField (max_length = 15)
	pCantidad = models.IntegerField ()
	pPrecioU = models.DecimalField(max_digits=7, decimal_places=2)
	pBase = models.DecimalField(max_digits=7, decimal_places=2)
	pIVA = models.DecimalField(max_digits=7, decimal_places=2)
	pTotal = models.DecimalField(max_digits=7, decimal_places=2)
	pPagarUS = models.IntegerField()
	pTotalUS = models.IntegerField()

	def __str__(self):
		return(f"{self.pRIF} {self.pDocumento} {self.pCliente} {self.pCliente} {self.pProducto}")

	class Meta:
		db_table = "details1"

