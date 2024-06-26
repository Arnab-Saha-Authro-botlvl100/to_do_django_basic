from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from home.templates import *
# Create your views here.

def home(request):
    return render(request, 'base.html', {'title': 'Home'})


def register(request):
    if request.method == 'POST':
        data = request.POST
        # print('asa')
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        repassword = data.get('repassword')

        if not all([email, password, name, repassword]):
            messages.error(request, "All fields are required")
            return render(request, 'register.html', {'title': 'Register'})

        if password != repassword:
            messages.error(request, "Password mismatch")
            return render(request, 'register.html', {'title': 'Register'})

        if User.objects.filter(username=email).exists():
            messages.error(request, "Email already exists")
            return render(request, 'register.html', {'title': 'Register'})

        # Create user
        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = name
        user.save()

        messages.success(request, 'You have successfully logged in.')
        return redirect('welcome')

    return render(request, 'register.html', {'title': 'Register'})

def user_login(request):
    if request.method == 'POST':
        data = request.POST
        email = data.get('email')
        password = data.get('password')

        if not all([email, password]):
            messages.error(request, "All fields are required")
            return render(request, 'login.html', {'title': 'Login'})
        
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful")
            return redirect('welcome')  # Redirect to the welcome page upon successful login
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'login.html', {'title': 'Login'})
