from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import authenticate, login, logout


from django.contrib.auth.decorators import login_required

@login_required
def lawyer_dashboard(request):
    return render(request, 'accounts/lawyer_dashboard.html')

@login_required
def client_dashboard(request):
    return render(request, 'accounts/client_dashboard.html')


def register_view(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']

        user = User.objects.create_user(
            username=username,
            password=password,
            role=role
        )

        return redirect('login')

    return render(request, 'accounts/register.html')


def login_view(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # ROLE BASED REDIRECT
            if user.role == 'lawyer':
                return redirect('lawyer_dashboard')
            else:
                return redirect('client_dashboard')

    return render(request, 'accounts/login.html')

def lawyer_dashboard(request):
    return render(request, 'accounts/lawyer_dashboard.html')

def client_dashboard(request):
    return render(request, 'accounts/client_dashboard.html')