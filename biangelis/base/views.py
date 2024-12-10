from django.shortcuts import render
from .models import Post

# Create your views here.

def home(request):
    return render(request, 'basis/home.html')

def feed(request):
    posts = Post.objects.all()

    context = {'posts':posts}
    return render(request, 'basis/feed.html', context)

def post(request):
    return render(request, 'basis/post.html')

def contact(request):
    return render(request, 'basis/contact.html')