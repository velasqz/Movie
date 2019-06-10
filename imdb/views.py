from django.views.generic import ListView, DetailView

from imdb.models import MovieRate, Movie


class HomeView(ListView):
    template_name = 'imdb/home.html'
    extra_context = {'title': 'My Internet movie database'}
    queryset = Movie.objects.all()
    paginate_by = 6

    def get_queryset(self):
        qs = super(HomeView, self).get_queryset()
        return qs.order_by('-id')

    def get_context_data(self, **kwargs):
        data = super(HomeView, self).get_context_data(**kwargs)
        best_movie = MovieRate.objects.get_best_rated().first()
        movie = Movie.objects.get(pk=best_movie.get('movie'))
        data.update({
            'best_rated_movie': movie,
            'best_rated_value': best_movie.get('rate'),
        })
        return data


class MovieDetailView(DetailView):
    queryset = Movie.objects.all()
    template_name = 'imdb/detail.movie.html'
    slug_field = 'title'
    query_pk_and_slug = False

