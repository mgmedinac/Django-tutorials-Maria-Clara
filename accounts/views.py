from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import UserCreateForm
from django.contrib.auth.forms import AuthenticationForm


def signupaccount(request):
    if request.method == 'GET':
        # Mostrar el formulario de registro
        return render(request, 'signupaccount.html', {'form': UserCreateForm()})
    else:
        # Procesar los datos enviados por el formulario
        if request.POST['password1'] == request.POST['password2']:
            try:
                # Intentar crear el usuario
                user = User.objects.create_user(
                    request.POST['username'],
                    password=request.POST['password1']
                )
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                # Nombre de usuario ya existe
                return render(request, 'signupaccount.html', {
                    'form': UserCreateForm(),
                    'error': 'Username already taken. Choose a new username.'
                })
        else:
            # Las contraseñas no coinciden
            return render(request, 'signupaccount.html', {
                'form': UserCreateForm(),
                'error': 'Passwords do not match.'
            })


def logoutaccount(request):
    logout(request)
    return redirect('home')


def loginaccount(request):
    if request.method == 'GET':
        return render(request, 'loginaccount.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )

        if user is None:
            return render(request, 'loginaccount.html', {
                'form': AuthenticationForm(),
                'error': 'Username and password do not match.'
            })
        else:
            login(request, user)
            return redirect('home')
