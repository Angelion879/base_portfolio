from django.shortcuts import render
from .models import Post

from .forms import PostForm

# Create your views here.

def home(request):
    context = {
        "repeat" : [1,2,3,4,5,6,7,8,9,10,12,13,14,15],
    }
    return render(request, 'basis/home.html', context)

def feed(request):
    posts = Post.objects.filter(active=True)

    context = {'posts':posts}
    return render(request, 'basis/feed.html', context)

def post(request):
    return render(request, 'basis/post.html')

def contact(request):
    return render(request, 'basis/contact.html')

# CRUD views

def createPost(request):
    form = PostForm()

    context = {'form':form}
    return render(request, 'base/post_form.html', context)