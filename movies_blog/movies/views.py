from django.shortcuts import render
from .models import Movies

def index(request):
    req_data = request.GET
    context = {
        'create_movie': req_data.get('data')
        if req_data else '영화가 없습니다'
    }
    return render(request, 'movies/index.html', context)
# Create your views here.

def create_movie(request):
    return render(request, 'movies/create_movie.html')

def new(request):
    req_data = request.GET
    context = {
        'create_movie': req_data.get('data')
    }
    return render(request, 'movies/new.html', context)

def index(request):
    movies = Movies.objects.all()
    context = {
        'movies' : movies
    }

    return render(request, 'movies/index.html', context)

def detail(request, movies_id):
    movies = Movies.objects.get(pk=movies_id)
    context = {
        'movies' : movies
    }
    return render(request, 'movies/detail.html', context)

