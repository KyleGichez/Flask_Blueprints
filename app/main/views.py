from webbrowser import get
from flask import render_template, make_response, session, request
from ..request import get_movies

from . import main

@main.route('/')
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

@main.route('/movies')
def movies():
    popular_movies = get_movies('popular')
    print(popular_movies)
    title = 'Welcome to the best movie review website'
    # context = dict()
    # context['popular_movies'] = get_movies('popular')
    # context['title'] = 'Welcome to the best movie review website'

    template = render_template('movies/movie.html', title = title, popular = popular_movies)
    response = make_response(template)
    return response


@main.route('/movie/<id>')
def movie(id):
    popular_movies = get_movies('popular')
    print(popular_movies)
    title = 'Welcome to the best movie review website'
    # context = dict()
    # context['popular_movies'] = get_movies('popular')
    # context['title'] = 'Welcome to the best movie review website'

    template = render_template('movies/movie.html', title = title, popular = popular_movies)
    response = make_response(template)
    return response