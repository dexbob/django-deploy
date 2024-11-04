from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.posts, name='posts'),
    path('posts/<slug:slug>', views.posts_detail, name='posts-detail'),
    path('posts-search/', views.posts_search, name='posts-search'),
]