from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, FormView

from mdb.forms import SimpleForm
from mdb.models import MovieRate, Movie
from django.contrib import messages

class HomeView(ListView):
    template_name = 'mdb/home.html'
    extra_context = {'title': 'My Internet movie database'}
    queryset = Movie.objects.all()
    paginate_by = 6

    def get_queryset(self):
        qs = super(HomeView, self).get_queryset()
        return qs.order_by('-id')

    def get_context_data(self, **kwargs):
        data = super(HomeView, self).get_context_data(**kwargs)
        best_movie = MovieRate.objects.get_best_rated().first()
        if best_movie:
            movie = Movie.objects.get(pk=best_movie.get('movie'))
            data.update({
                'best_rated_movie': movie,
                'best_rated_value': best_movie.get('rate', 0),
            })
            return data


class MovieDetailView(LoginRequiredMixin, DetailView):
    queryset = Movie.objects.all()
    template_name = 'mdb/detail.movie.html'
    slug_field = 'slug'
    query_pk_and_slug = False


class MovieFormExample(CreateView):
    template_name = 'mdb/simple.form.example.html'
    form_class = SimpleForm
    success_url = '.'

    def form_invalid(self, form):
        return super(MovieFormExample, self).form_invalid(form)

    def get_form_kwargs(self):
        kwargs = super(MovieFormExample, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs