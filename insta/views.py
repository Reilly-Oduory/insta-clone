from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import RegistrationForm, ProfileForm, UpdateProfileForm, NewPostForm, UpdateCaptionForm, CommentForm
from .models import Comment, Post, Profile, Tag, User

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
    posts = Post.objects.filter(user=user).all()
    tags = []
    for post in posts:
        tags.append(post.tags)
    context = {"profile":profile, "posts":posts, "tags":tags}
    return render(request, 'profile/view_profile.html', context)


# homepage
@login_required(login_url='/login/')
def home(request):
    user = request.user
    posts = Post.objects.all()
    context = {"user":user, "posts":posts}
    return render(request, 'home.html', context)

# Posts
@login_required(login_url='/login/')
def new_post(request):
    form = NewPostForm()
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.likes = 0
            obj.save()
            messages.success(request, "Post Successfully created.")
            return redirect(f'/post/{obj.id}/')
        else:
            messages.error(request, "Post procedure failed")

    context = {"form":form}
    return render(request, 'post/new_post.html', context)

def add_tag(request):
    if request.method == 'POST':
        if 'new_tag' in request.POST and request.POST["new_tag"]:
                tag_name = request.POST.get("new_tag")
                tag = Tag()
                tag.tag = tag_name
                tag.save_tag()
    
    return redirect(f'/new_post/')


@login_required(login_url='/login/')
def view_post(request, post_id):
    post = Post.objects.filter(id=post_id).first()
    comments = Comment.objects.filter(post=post).all()
    context = {"post":post, "comments":comments}
    return render(request, 'post/post.html', context)

@login_required(login_url='/login/')
def like(request, post_id):
    post = Post.objects.filter(id=post_id).first()
    post.post_like()
    context = {"post":post}
    return redirect(f'/post/{post_id}/')

@login_required(login_url='/login/')
def update_post_caption(request, post_id):
    post = Post.objects.filter(id=post_id).first()
    if request.user == post.user:
        form = UpdateCaptionForm()
        if request.method == 'POST':
            form = UpdateCaptionForm(request.POST)
            if form.is_valid():
                new_caption = form.cleaned_data.get('caption')
                post.update_caption(new_caption)
                messages.success(request, "Caption successfully changed")
                return redirect(f'/profile/')
            else:
                messages.error(request, "Caption update failed")
        
    else:
        messages.error(request, "Cannot edit caption")
        return redirect(f'/post/{post_id}/')

    context = {"form":form}
    return render(request, 'post/update_caption.html', context)

# Comments
@login_required(login_url='/login/')
def new_comment(request, post_id):
    post = Post.objects.filter(id=post_id).first()
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.post = post
            obj.user = request.user
            obj.save()
            messages.success(request, "Comment sent")
            return redirect(f'/post/{post_id}/')        

    context = {"form":form}

    return render(request, 'comments/new_comment.html', context)

# search
@login_required(login_url='/login/')
def search(request):
    if 'search' in request.GET and request.GET["search"]:
        search_term = request.GET.get("search")
        search_results = User.objects.filter(username__icontains=search_term).all()
        message = f"{search_term}"
        return render(request, 'search.html', {"message": message, "search_results":search_results})
    else: 
        message = "You haven't searched for anything yet"
        return render(request, "search.html", {"message": message})

@login_required(login_url='/login/')
def searched_user(request, username):
    user = User.objects.filter(username=username).first()
    posts = Post.objects.filter(user=user).all()
    context = {"posts":posts, "user":user}

    return render(request, 'individual_user.html', context)