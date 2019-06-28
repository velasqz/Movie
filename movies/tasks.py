from django.http import HttpResponse
from movies.celery import app
from movies.proces_movie import *


@app.task()
def get_movie(type , value):
    data = connection(type, value)
    movie = save_movies(data)
    return movie

@app.task()
def send_email_to_user():
   sendmail()

