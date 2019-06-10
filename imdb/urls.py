from django.urls import path

from imdb.views import HomeView, MovieDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('movies/<slug>/', MovieDetailView.as_view(), name='movie-detail')
]