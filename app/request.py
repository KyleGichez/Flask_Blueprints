from . import create_app
from flask import current_app

api_key = create_app.config['MOVIE_API_KEY']