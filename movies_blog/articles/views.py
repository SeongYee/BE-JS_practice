from django.shortcuts import render, redirect
from .models import Article

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)
# Create your views here.

def detail(request, pk):
    articles = Article.objects.get(pk=pk)
    context = {
        'articles' : articles
    }

    return render(request, 'articles/detail.html', context)

def create(request):
    return render(request, 'articles/create.html')

def save(request):
    data = request.POST
    # article = Article()
    # article.title = data.get('title')
    # article.content = data.get('content')
    # article.save()
    Article.objects.create(title=data.get('title'), content=data.get('content'))
    return render(request, 'articles/save.html')

def save(request):
    data = request.POST
    new_article = Article.objects.create(title=data.get('title'), content=data.get('content'))
    return redirect('articles:detail', pk = new_article.pk)

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article':article
    }
    return render(request, 'articles/edit.html', context)