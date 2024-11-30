from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'basis/home.html')

def feed(request):
    return render(request, 'basis/feed.html')

def post(request):
    return render(request, 'basis/post.html')

def contact(request):
    return render(request, 'basis/contact.html')