from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile 

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user) 
            return redirect('predict_osteoporosis')  
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')  
    
    return render(request, 'login.html')  

def index_view(request):
    username_initial = request.user.username[0].upper()  
    return render(request, 'index.html', {'username_initial': username_initial})
 

def logout_view(request):
    logout(request)
    return redirect('login')  

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "An account with this email already exists.")
            return redirect('signup')

        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            UserProfile.objects.create(user=user, email=email, username=username)

            login(request, user)

            messages.success(request, "Account created successfully!")
            return redirect('login')  
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return redirect('signup')
    
    return render(request, 'signup.html')