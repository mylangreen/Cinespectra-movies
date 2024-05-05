from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('movies/',views.movie_list,name='movie_list'),
    path('series/',views.series,name='series'),
    path('<int:pk>/',views.detail_view,name='detail'),
    path('genre/<int:pk>/<str:movie_type>/',views.genre_view,name='genre'),
    path('search/q',views.search_view,name='search'),
    path('request/',views.request_view,name='request'),
    path('thank-you/',views.thank_you,name='thankyou'),
    path('season/episode/<int:pk>/',views.season_view,name='season')
]

