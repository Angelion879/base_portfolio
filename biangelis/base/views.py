from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<h2>Home Page</h2>')

def feed(request):
    return HttpResponse('<h2>Posts feed</h2>')

def post(request):
    return HttpResponse('<h2>Post page</h2>')

def profile(request):
    return HttpResponse('<h2>Profile</h2>')