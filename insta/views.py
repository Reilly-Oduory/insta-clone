from django.shortcuts import render, redirect
from .forms import RegistrationForm

# Create your views here.
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/')
        
    context = {"form":form}
    return render(request, 'auth/register.html', context)

def login(request):
    context = {}
    return render(request, 'auth/login.html', context)

def home(request):
    context = {}
    return render(request, 'home.html', context)