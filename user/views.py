from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError

# Create your views here.


def signUp(request):
    if request.method == 'GET':
        return render(request, 'user/signUp.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'user/signUp.html', {'form': UserCreationForm(), 'error': 'Your username is already has signed up!'})
        else:
            return render(request, 'user/signUp.html', {'form': UserCreationForm(), 'error': 'Passwords are not match!'})


def logoutUser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    else:
        pass

def loginUser(request):
    if request.method == 'GET':
        return render(request , 'user/login.html' , {'form':AuthenticationForm()})
    else:
        user = authenticate(request , username = request.POST['username'] , password = request.POST['password'])

        if user is None:
            return render(request , 'user/login.html' , {'form':AuthenticationForm() , 'error':'Username or Password did not match!'})
        else:
            login(request , user)
            return redirect('home')
