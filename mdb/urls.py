from django.urls import path

from mdb.views import HomeView, MovieDetailView, MovieFormExample

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('movies/<slug>/', MovieDetailView.as_view(), name='movie-detail'),
    path('form/', MovieFormExample.as_view(), name='simple-form')
]