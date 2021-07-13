from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404

from .forms import RegistrationForm, ProfileForm, UpdateProfileForm
from .models import Profile

# Create your views here.
def register_user(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            messages.success(request, "You have successfully Signed Up")
            return redirect(f'/add_profile/')
        
    context = {"form":form}
    return render(request, 'auth/register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in")
            return redirect(f'/')
        else:
            messages.info(request, "The Username or Password is incorrect")

    context = {}
    return render(request, 'auth/login.html', context)

@login_required(login_url='/login/')
def logout_user(request):
    logout(request)
    return redirect('/login')

# profile
@login_required(login_url='/login/')
def create_profile(request):
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            messages.success(request,"Profile Successfully created")
            return redirect(f'/profile')
        else:
            messages.info(request, "Form submision failed")

    username = request.user.username
    context={"form":form, "username":username}
    return render(request, 'auth/create_profile.html', context)

@login_required(login_url='/login/')
def update_profile(request):
    username = request.user.username
    profile = Profile.objects.filter(user=request.user).first()
    form = UpdateProfileForm()
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST)
        if form.is_valid():
            bio = form.cleaned_data.get('bio')
            Profile.update_profile_bio(profile, bio)
            messages.success(request,"Profile Successfully created")
            return redirect(f'/profile')
        else:
            messages.info(request, "Update Profile procedure failed")
    context = {"form":form, "username":username}
    return render(request, 'profile/update_profile.html', context)

@login_required(login_url='/login/')
def view_profile(request):
    user = request.user
    profile = Profile.objects.filter(user=user).first()
    context = {"profile":profile}
    return render(request, 'profile/view_profile.html', context)


# homepage
@login_required(login_url='/login/')
def home(request):
    user = request.user
    context = {"user":user}
    return render(request, 'home.html', context)