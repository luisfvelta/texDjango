from django.urls import path
from . import views                 

urlpatterns = [
	path('act_doc/<int:pk>', views.actualiza_doc, name='update_doc'),
	path('agr_doc/', views.agrega_doc, name='agrega_doc'),	
	path('car_doc/', views.carga_doc, name='carga_doc'),	
	path('eli_doc/<int:pk>', views.elimina_doc, name='eli_doc'),

]


	


