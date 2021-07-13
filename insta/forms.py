from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm, fields

from .models import User, Profile

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['fullname', 'profile_pic', 'bio']

class UpdateProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['bio']