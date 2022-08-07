from flask import create_app
import urllib.request,json
from .models import movie

Movie = movie.Movie

api_key = create_app.config['MOVIE_API_KEY']

base_url = create_app.config['MOVIE_BASE_URL']