from django.urls import path

from mdb.views import HomeView, MovieDetailView, MovieFormExample, MovieListView, MovieRateDetailView, MovieRateListView, \
            MovieRateCreateView, MovieRateUpdateView, MovieRateDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('form/', MovieFormExample.as_view(), name='simple-form'),
    path('movie/', MovieListView.as_view(), name='drf-movie-list'),
    path('movie/<slug>/', MovieDetailView.as_view(), name='drf-movie-detail'),
    path('movierate/', MovieRateListView.as_view(), name='drf-movierate-list'),
    path('movierate/<int:pk>/', MovieRateDetailView.as_view(), name='drf-movierate-detail'),
    path('movieratecreate/', MovieRateCreateView.as_view(), name='drf-movierate-create'),
    path('movierateupdate/<int:pk>/', MovieRateUpdateView.as_view(), name='drf-movierate-update'),
    path('movieratedelete/<int:pk>/', MovieRateDeleteView.as_view(), name='drf-movierate-delete'),


]