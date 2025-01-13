from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from . import views

urlpatterns =[
    path('', views.home, name="home"),
    path('feed/', views.feed, name="feed"),
    path('post/<slug:slug>/', views.post, name="post"),
    path('contact/', views.contact, name="contact"),

    # Language path
    path('i18n/', include('django.conf.urls.i18n')),

    # CRUD paths
    path('create_post/', views.createPost, name="create_post"),
    path('update_post/<slug:slug>/', views.updatePost, name="update_post"),
    path('delete_post/<slug:slug>/', views.deletePost, name="delete_post"),
]