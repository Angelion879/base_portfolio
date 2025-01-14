from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _, get_language
from base.generator import home_repeat, wlpp_repeat

from .models import Post
from .forms import PostForm

# Create your views here.

def home(request):
    repeat = home_repeat()

    context = {'repeat':repeat}
    return render(request, 'basis/home.html', context)

def feed(request):
    user_lang = get_language()
    print(user_lang)
    if str(user_lang) == 'en':
        posts = Post.objects.filter(language='en', active=True)
    else:
        posts = Post.objects.filter(language='pt', active=True)

    context = {'posts':posts}
    return render(request, 'basis/feed.html', context)

def post(request, slug):
    content = Post.objects.get(slug=slug)
    repeat = wlpp_repeat()

    context = {'post':content, 'repeat':repeat}
    return render(request, 'basis/post.html', context)

def contact(request):
    return render(request, 'basis/contact.html')

# CRUD views

@login_required(login_url="home")
def create_post(request):
    form = PostForm()
    repeat = wlpp_repeat()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('feed')

    context = {'form':form, 'repeat':repeat}
    return render(request, 'basis/post_form.html', context)

@login_required(login_url="home")
def update_post(request,slug):
    up_post = Post.objects.get(slug=slug)
    form = PostForm(instance=up_post)
    repeat = wlpp_repeat()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=up_post)
        if form.is_valid():
            form.save()
        return redirect('feed')

    context = {'form':form, 'repeat':repeat}
    return render(request, 'basis/post_form.html', context)

@login_required(login_url="home")
def delete_post(request,slug):
    del_post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        del_post.delete()
        return redirect('feed')
    context={'item':del_post}
    return render(request, 'basis/delete.html', context)
