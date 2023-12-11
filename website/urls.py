from django.urls import path
from . import views                 

urlpatterns = [
	path('', views.home, name='home'),
	path('agrega_cliente/', views.agrega_cliente, name='agrega_cliente'),	
	path('agrega_producto/', views.agrega_producto, name='agrega_producto'),	
	path('cliente/<int:pk>', views.registro_cliente, name='cliente'),	
	path('delete_record/<int:pk>', views.delete_record, name='delete_record'),	
	path('logout/', views.logout_user, name='logout'),
	#path('record/<int:pk>', views.customer_record, name='record'),
	path('register/', views.register_user, name='register'),
	path('update_record/<int:pk>', views.update_record, name='update_record'),
	
]

