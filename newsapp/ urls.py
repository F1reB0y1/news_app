from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news_list, name='news_list'),
    path('news/<pk>/', views.news_detail, name='news_detail'),
    path('authors/', views.author_list, name='author_list'),
    path('authors/<pk>/', views.author_detail, name='author_detail'),
    path('authors/<pk>/news/', views.author_news_list, name='author_news_list'),
]