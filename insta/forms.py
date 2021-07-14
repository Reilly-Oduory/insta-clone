from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm, fields

from .models import Comment, Post, Tag, User, Profile

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    username = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "Enter Username"}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "Enter Email"}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "Enter Password"}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "Confirm Password"}))

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['fullname', 'profile_pic', 'bio']

    fullname = forms.CharField(widget=(forms.TextInput(attrs={'class': "form-control", 'placeholder': "Enter your Fullname"})))
    profile_pic = forms.ImageField.widget.attrs={'class': "form-control"}
    bio =forms.CharField(widget=(forms.Textarea(attrs={'class': "form-control", 'placeholder': "Tell us more about your self", 'cols': "25"})))

class UpdateProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['bio']

class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['tag']


class NewPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'caption', 'location', 'tags']

    tags = forms.ModelMultipleChoiceField(
        queryset = Tag.objects.all(),
        widget = forms.CheckboxSelectMultiple
    )

class UpdateCaptionForm(ModelForm):
    class Meta:
        model = Post
        fields = ['caption']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']