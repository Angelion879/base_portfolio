from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _, get_language
from base.generator import home_repeat, post_repeat

from .models import Post
from .forms import PostForm

# Create your views here.

def home(request):
    user_lang = get_language()
    print(user_lang)
    repeat = home_repeat()

    context = {'repeat':repeat}
    return render(request, 'basis/home.html', context)

def feed(request):
    posts = Post.objects.filter(active=True)

    context = {'posts':posts}
    return render(request, 'basis/feed.html', context)

def post(request, slug):
    post = Post.objects.get(slug=slug)
    repeat = post_repeat()

    context = {'post':post, 'repeat':repeat}
    return render(request, 'basis/post.html', context)

def contact(request):
    return render(request, 'basis/contact.html')

# CRUD views

@login_required(login_url="home")
def createPost(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('feed')

    context = {'form':form}
    return render(request, 'basis/post_form.html', context)

@login_required(login_url="home")
def updatePost(request,slug):
    post = Post.objects.get(slug=slug)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
        return redirect('feed')

    context = {'form':form}
    return render(request, 'basis/post_form.html', context)

@login_required(login_url="home")
def deletePost(request,slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        post.delete()
        return redirect('feed')
    context={'item':post}
    return render(request, 'basis/delete.html', context)
