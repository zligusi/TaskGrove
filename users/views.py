from django.shortcuts import render , redirect
from django.contrib.auth import login
from django.contrib.auth import authenticate
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main:home')
    else:
        form = RegistrationForm()
        return render(request, 'users/register.html', {'form': form})


def login_view (request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user :
            login(request, user)
            return redirect('main:home')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'users/login.html')