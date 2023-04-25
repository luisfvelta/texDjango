from django.shortcuts import render, redirect
	
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from .forms import SignUpForm, AgregaCliente, AgregaProducto

from .models import Cliente

def add_record(request):
	form = AgregaCliente(request.POST or None)  

	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid:
				add_record = form.save()
				messages.success(request, "registro agregado!")
				return redirect('home')
		return render(request,'add_record.html', {'form':form})
	else:
		messages.success(request, "Debes haber efectuado login")
		return redirect('home')

def add_producto(request):
	form = AgregaProducto(request.POST or None)  

	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid:
				add_producto = form.save()
				messages.success(request, "registro agregado!")
				return redirect('home')
		return render(request,'add_producto.html', {'form':form})
	else:
		messages.success(request, "Debes haber efectuado login")
		return redirect('home')

def customer_record(request,pk):
	if request.user.is_authenticated:
		customer_record = Cliente.objects.get(id=pk)
		return render(request,'record.html',{'customer_record':customer_record})
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
			messages.success(request,username + " You have been logged in")
			return redirect ('home')
		else:
			messages.success(request,username + " There was an error")
			return redirect ('home')
	else:
		records = Cliente.objects.all()
		return render(request,'home.html', {'records':records})

def logout_user(request):
	logout(request)
	messages.success(request, "You have  logged out")
	return redirect ('home')


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
			messages.success(request, username + " You have successfully registered! Welcome")
			return redirect('home')

		else:
			form = SignUpForm()
			return render(request,'register.html',{'form':form})


	return render(request,'register.html',{'form':form})


def update_record(request, pk):

	if request.user.is_authenticated:
		current_record = Cliente.objects.get(id=pk)
		print(current_record)

		form = AgregaCliente(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request,"Datos actualizados")
			return redirect('home')
		return render(request,'update_record.html',{'form':form})
	else:
		messages.success(request," Login requerido para acceder a esta función")
		return redirect('home')


		




	
	