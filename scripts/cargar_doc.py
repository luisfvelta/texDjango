# views sygbv

from .models import Documento

import csv

def run():
	fn = 'C:/97LUIS/sygbv/rawdata/sygbvdata/Ventas2022.csv'	
	totCantidad = 0
	totPrecioU = 0
	totBase = 0
	totIVA = 0
	totTotal = 0
 	totTotalUS = 0
	totPagarUS = 0
	totTotalUS = 0
	print(f'Opening file {fn}')
	with open(fn,'r') as f:
		datos = csv.DictReader(f)
		for row in datos:
			print(row)
			try:
				pagarUS=int(row[12])
			except:
				pagarUS=0
			try:
				totalUS=int(row[13])
			except:
				totalUS=0
			try:
				cantidad=int(row["Cantidad"])
			except:
				cantidad=0
			doc = Documento(pFecha=row["Fecha"],
		        pDocumento=row["Documento"],
		        pControl=row["Control"],
		        pCliente=row["Cliente"],
		        pRIF=row["RIF"],
		        pProducto = row["Producto"],		        
		        	            
		        pPrecioU = float(row["PrecioU"]),
		        pBase = float(row["BaseB"]),
		        pIVA = float(row["IVA"]),
		        pTotal = float(row["Total"]), 

		        pCantidad = cantidad,	
		        pTotalUS = totalUS,
		        pPagarUS = pagarUS)
			try:
				doc.save()
			except:
				print(f"There was a problem with {pDocumento}")
	print("fin de carga de datos")
	                    
        

    


        




