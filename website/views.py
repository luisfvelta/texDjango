from django.shortcuts import render, redirect
	
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from .forms import SignUpForm, AgregaCliente, AgregaProducto

from .models import Cliente
from .models import Producto

def agrega_cliente(request):
	form = AgregaCliente(request.POST or None)  

	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid:
				agrega_cliente = form.save()
				messages.success(request, "Se agregó el cliente con el rut: " + agrega_cliente.rut)
				return redirect('home')
		return render(request,'agrega_cliente.html', {'form':form})
	else:
		messages.success(request, "Debes haber efectuado login")
		return redirect('home')

def registro_cliente(request,pk):
	if request.user.is_authenticated:
		registro_cliente = Cliente.objects.get(id=pk)
		return render(request,'cliente.html',{'registro_cliente':registro_cliente})
	else:
		messages.success(request, " You Must Be Logged In to View That Page!")
		return redirect('home')

def delete_record(request,pk):
	if request.user.is_authenticated:
		delete_it = Cliente.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully")
		return redirect('home')
	else:
		messages.success(request, " You Must Be Logged In to do that!")
		return redirect('home')

def update_record(request, pk):

	if request.user.is_authenticated:
		cliente_actual = Cliente.objects.get(id=pk)
		
		form = AgregaCliente(request.POST or None, instance=cliente_actual)
		if form.is_valid():
			form.save()
			messages.success(request,"Datos actualizados para " + cliente_actual.rut)
			return redirect('home')
		return render(request,'update_record.html',{'form':form})
	else:
		messages.success(request," Login requerido para acceder a esta función")
		return redirect('home')

def agrega_producto(request):
	form = AgregaProducto(request.POST or None)  

	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid:
				agrega_producto = form.save()
				messages.success(request, "registro agregado!")
				return redirect('home')
		return render(request,'agrega_producto.html', {'form':form})
	else:
		messages.success(request, "Debes haber efectuado login")
		return redirect('home')



def home(request):
	#records = Record.objects.all()

	# Check to see if logging in
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		# Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request,username + " Bienvenido. Has efectuado tu login!")
			return redirect ('home')
		else:
			messages.success(request,username + " Intento errado!")
			return redirect ('home')
	else:
		clientes = Cliente.objects.all()
		return render(request,'home.html', {'clientes':clientes})


def register_user(request):
	form=SignUpForm(request.POST)
	if request.method == "POST":
		
		if form.is_valid():
			form.save()
			# Authenticate and log in
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username = username, password = password)
			login(request,user)
			messages.success(request, username + " Te has registrado. Bienvenido")
			return redirect('home')

		else:
			form = SignUpForm()
			return render(request,'register.html',{'form':form})


	return render(request,'register.html',{'form':form})



def logout_user(request):
	logout(request)
	messages.success(request, "Hasta luego. Has salido del sistema!")
	return redirect ('home')



		




	
	