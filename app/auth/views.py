from re import template
from flask import render_template, make_response, session, request

from . import auth
from . import movies

@auth.route('/')
def login():
    content = dict()
    content['title'] = 'Gichez D Man'
    content['first_name'] = 'Sexy Ms Dollar Baby'
    content['email'] = 'kylegichez@gmail.com'
    content['amount'] = '$15,000'
    content['phone'] = '0712345678'

    template = render_template('auth/index.html', content = content)
    response = make_response(template)
    return response

@movies.route('/movies/<movie_id>')
def movies(movie_id):

    template = render_template('movies/movie.html', id = movie_id)
    response = make_response(template)
    return response