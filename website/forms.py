from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Cliente, Producto


class AgregaCliente(forms.ModelForm):
	rut = forms.CharField(label="",required=True,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'RUT'}))
	descripcion = forms.CharField(label="",required=True,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Descripcion'}))
	email = forms.CharField(label="",required=True,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}))
	telefono = forms.CharField(label="",required=True,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Teléfono'}))
	direccion = forms.CharField(label="",required=True,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Dirección'}))
	ciudad = forms.CharField(label="",required=True,widget=forms.TextInput(attrs={'class':'form-control ', 'placeholder':'Ciudad'}))
	comuna = forms.CharField(label="",required=True,widget=forms.TextInput(attrs={'class':'form-control ', 'placeholder':'Comuna'}))
	region = forms.CharField(label="",required=True,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Región'}))
	codigo_postal = forms.CharField(label="",required=True,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Código Postal'}))

	class Meta():
		model = Cliente
		exclude = ("user",)

class AgregaProducto(forms.ModelForm):
	familia = forms.CharField(label="",required=True,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Familia'}))
	descripcion = forms.CharField(label="",required=True,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Descripcion'}))
	marca = forms.CharField(label="",required=True,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Marca'}))
	proveedor = forms.CharField(label="",required=True,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Proveedor'}))
	unidad_medida  = forms.CharField(label="",required=True,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Unidad de medida'}))
	peso_en_gramos = forms.IntegerField(label="",required=True,widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Peso'}))
	costo_unitario = forms.DecimalField(label="",required=True,widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Costo Unitario'}))
	precio_detal = forms.DecimalField(label="",required=True,widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Precio Detal'}))
	precio_canal = forms.DecimalField(label="",required=True,widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Precio Canal'}))
	precio_fabricante = forms.DecimalField(label="",required=True,widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Precio Fabricante'}))
	precio_lista = forms.DecimalField(label="",required=True,widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Precio Lista'}))
	precio_corporativo = forms.DecimalField(label="",required=True,widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Precio Corporativo'}))
	existencias = forms.IntegerField(label="",required=True,widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Existencias'}))



	class Meta():
		model = Producto
		exclude = ("user",)


class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}))
	nombre = forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}))
	apellido = forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido'}))

	class Meta:
		model = User
		fields = ('username','nombre','apellido','email','password1','password2')


	def __init__(self, *args, **kwargs):

		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'Usuario'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form_text text_muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. </small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''

		#self.fields['password1'].help_text = '<ul class="form_text text_muted> <small"><li>Your password can not be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can not be a commonly used password.</li><li>Your password can not be entirely numeric.</li></small></ul>' 
		
		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirme su Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form_text text_muted"><small>Enter the same password as before, for verification.</small></span>'





