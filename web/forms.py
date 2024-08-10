from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import ContactForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactFormForm(forms.Form):
    
    customer_email = forms.EmailField (label='Correo')
    customer_name = forms.CharField (max_length=64, label='Nombre')
    message = forms.CharField (label='Mensaje')


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Nombre de Usuario')
    first_name = forms.CharField(max_length=140, required=True, label='Nombre')
    last_name = forms.CharField(
        max_length=140, required=False, label='Apellido')
    email = forms.EmailField(required=True, label='Email')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirmar Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email', 'password1', 'password2']
        labels = {'username': 'Nombre de usuario', 'first_name': 'Nombre del Cliente', 'last_name': 'Apellido del Cliente','email': 'Email', 'password1': 'Contraseña', 'password2': 'Confirme Contraseña'}


class  ContactFormModelForm(ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_email','customer_name','message']
        labels = {'customer_email':'Email del cliente', 'customer_name':'Nombre del cliente', 'message':'Mensaje'}

