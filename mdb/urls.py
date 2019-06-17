from django.urls import path

from mdb.views import HomeView, MovieDetailView, MovieFormExample, MovieListView, MovieRateDetailView, MovieRateListView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('form/', MovieFormExample.as_view(), name='simple-form'),
    path('movie/', MovieListView.as_view(), name='drf-movie-list'),
    path('movie/<slug>/', MovieDetailView.as_view(), name='drf-movie-detail'),
    path('movierate/', MovieRateListView.as_view(), name='drf-movierate-list'),
    path('movierate/<int:pk>/', MovieRateDetailView.as_view(), name='drf-movierate-detail')
]