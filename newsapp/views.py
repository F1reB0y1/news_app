from django.shortcuts import render
from .models import News, Author

def home(request):
    latest_news = News.objects.all().order_by('-date_of_publication')[:10]
    return render(request, 'home.html', {'latest_news': latest_news})

def news_list(request):
    all_news = News.objects.all().order_by('-date_of_publication')
    return render(request, 'news_list.html', {'all_news': all_news})

def news_detail(request, pk):
    news = News.objects.get(pk=pk)
    return render(request, 'news_detail.html', {'news': news})

def author_list(request):
    all_authors = Author.objects.all()
    return render(request, 'author_list.html', {'all_authors': all_authors})

def author_detail(request, pk):
    author = Author.objects.get(pk=pk)
    return render(request, 'author_detail.html', {'author': author})

def author_news_list(request, pk):
    author = Author.objects.get(pk=pk)
    news_list = author.news_set.all()
    return render(request, 'author_news_list.html', {'author': author, 'news_list': news_list})