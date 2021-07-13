from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm, fields

from .models import Comment, Post, Tag, User, Profile

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