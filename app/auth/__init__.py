from flask import Blueprint

auth = Blueprint('auth', __name__)
movies = Blueprint('movies', __name__)

from . import views