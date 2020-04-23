from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import User

def LoginView(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            usr = User.objects.filter(is_active=True)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
            else:
                messages.error(request, "You ar seeing this because, either the credentials does not belong to any account or the account has not been activated.")
                return redirect('login')
        return render(request, 'login.html')
    return redirect('home')

@login_required
def LogoutView(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out. Please login to continue!')
    return redirect('login')

def RegisterView(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            try:
                user = User.objects.get(username=username)
            except:
                user = None
            if user is None:
                user = User()
                user.username = username
                user.set_password(password)
                user.is_active = False
                user.save()
                messages.success(request, 'Your account has been successfully created. Please complete the payment for activating you account.')
                return redirect('login')
            else:
                messages.error(request, 'A user already exists in this name. Please try a different username.')
                return redirect('register')
        return render(request, 'register.html')
    else:
        return redirect('login')