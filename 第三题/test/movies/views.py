from django.shortcuts import render
from .models import Movie

def index(requset):

    movies = Movie.objects.order_by('id')
    context = {'movies': movies}
    return render(requset, 'movies/index.html', context)
def movie(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    context={'movie':movie}
    return render(request,'movies/movie.html',context)

