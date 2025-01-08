from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name="home"),
    path('feed/', views.feed, name="feed"),
    path('post/<slug:slug>/', views.post, name="post"),
    path('contact/', views.contact, name="contact"),

    # CRUD paths
    
    path('create_post/', views.createPost, name="create_post"),
]