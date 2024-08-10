from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import ContactForm, Tecnologia
from .forms import ContactFormForm, ContactFormModelForm, UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.


def indice(request):
    public_tecnologias = Tecnologia.objects.filter(is_private=False)
    return render(
        request,
        'index.html',
        {
            'public_tecnologias': public_tecnologias
        }
    )

def acerca(request):
    return render(request, 'about.html', {})


def bienvenido(request):
    return render(request, 'welcome.html', {})


@login_required
def bienvenido(request):
    private_tecnologias = Tecnologia.objects.filter(is_private=True)
    return render(
        request,
        'welcome.html',
        {
            'private_tecnologias': private_tecnologias
        }
    )


def contacto(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/exito')
    else:
        form = ContactFormModelForm()
    return render(request, 'contactus.html', {'form': form})


def exito(request):
    return render(request, 'success.html', {})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            return HttpResponseRedirect('/exito_registro')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})


def exito_registro(request):
    return render(request, 'exito_registro.html', {})


def nutricion(request):
    return render(request, 'nutricion.html', {})


def clima(request):
    return render(request, 'clima.html', {})

