from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name="home"),
    path('feed/', views.feed, name="feed"),
    path('post/', views.post, name="post"),
    path('contact/', views.contact, name="contact"),
]