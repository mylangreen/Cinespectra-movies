from django.shortcuts import render,get_object_or_404,redirect
from .models import Movie,Category,Cast,MovieRequest,Season,Episode
from django.core.mail import send_mail
from Cinespectra import settings


# Create your views here.
def index(request):
    hot = Movie.objects.get(hot=True)
    trending = Movie.objects.filter(is_trending=True)[::-1]
    upcoming = Movie.objects.filter(is_upcoming=True)
    genres  = Category.objects.all()
    return render(request,'index.html',{
        'hot': hot,
        'trending': trending,
        'upcoming': upcoming,
        'genres': genres,
        })


def movie_list(request):
    movies = Movie.objects.filter(type="Single").filter(is_upcoming=False)[::-1]
    genres  = Category.objects.all()
    return render(request,'movie_list.html',{
        'movies': movies,
        'genres': genres,
        })

def series(request):
    movies = Movie.objects.filter(type="Seasonal").filter(is_upcoming=False)[::-1]
    genres  = Category.objects.all()
    return render(request,'series.html',{
        'movies': movies,
        'genres': genres,
    })


def detail_view(request,pk):
    movie = get_object_or_404(Movie,pk=pk)
    cast = movie.cast.all()[::1]
    icon_code = ''
    if movie.type == "Single":
       similar_movies = Movie.objects.filter(genre=movie.genre.first()).exclude(pk=pk).filter(type="Single")[0:8]
       movie_type = 'Single'
    else:
       similar_movies = Movie.objects.filter(type="Seasonal").filter(genre=movie.genre.first()).exclude(pk=pk).distinct()[0:8]
       movie_type = 'Seasonal'
    return render(request,'detail.html',{
        'movie': movie,
        'similar_movies': similar_movies,
        'cast': cast,
        'movie_type': movie_type,
    })

def genre_view(request,pk,movie_type):
    category = get_object_or_404(Category,pk=pk)
    movies = Movie.objects.filter(genre=category, type=movie_type).filter(is_upcoming=False)
    
    return render(request,'genre.html',{
        'movies': movies,
        'category': category,
    })

def search_view(request):
    query=request.GET.get('search')
    
    if query:
        movies = Movie.objects.filter(is_upcoming=False).filter(title__icontains=query)
    else:
       movies = []
    return render(request,'search.html',{
        'movies': movies,
        'query': query,
    }) 

def thank_you(request):
    return render(request,'thank_you.html')

def request_view(request):
    if request.method=="POST":
       movie_title = request.POST.get('movie')
       name = request.POST.get('name')
       email = request.POST.get('email')
       MovieRequest.objects.create(title=movie_title,name=name)
       subject = 'New Movie Request'
       message = 'You have recieved a new movie request\nFrom:'+name+"\nTitle:"+movie_title
       from_email = email
       to_list = [settings.EMAIL_HOST_USER]
       send_mail(
           subject,
           message,
           from_email,
           to_list,
           fail_silently=False,   
       )
       return redirect('thankyou')
    return render(request,'request.html')

def season_view(request,pk):
    season = get_object_or_404(Season,pk=pk)
    return render(request,'episode.html',{
        'season': season,
    })   
        