import requests
from mdb.forms import SearchMovie
from mdb.models import Movie
from django.core.mail import send_mail


def connection(type_search , title):
    api_key = '7466d5ca'
    url = 'http://www.omdbapi.com/?{}={}&apikey={}'.format(type_search ,title , api_key)
    data = requests.get(url)
    if data.status_code == 200:
        data_movie = data.json()
        return data_movie
    else:
        return 'Conection Failed'

def save_movies(data):
    if data['Response'] == 'True':
        info_movies_search = data.get('Search' ,None)
        if info_movies_search is not None:
            pass
        else:
            info_movies_search = []
            info_movies_search.append(data)

        for info_movie_web in info_movies_search:
            movie = Movie()
            movie.title = info_movie_web['Title']
            movie.genere = info_movie_web.get('Genre', 'No register')
            movie.director = info_movie_web.get('Director', 'No register')
            movie.duration = info_movie_web.get('Duration', '2:00')
            movie.save()
        return "sussefully"
    return 'Movie no found'

def sendmail():
    send_mail(
        'Email Example',
        'movie create succefully',
        'jmoreno@lsv-tech.com',
        ['javiergmorenovelasquez@solucionescalamari.com'],
        fail_silently=False,
    )

    return 'Email sended'



