from flask import current_app

import json, urllib.request, requests

from .models import Movie

def get_movies(category):
    # current_app.config.get()
    base_url = current_app.config.get('MOVIE_API_BASE_URL')
    get_movies_url = f"{base_url}/{category}{current_app.config.get('MOVIE_API_PAYLOAD')}"
    
    
    movie_results = None
    # print(get_movies_url)
    # get_movies_data = requests.get(get_movies_url)
    with urllib.request.urlopen(get_movies_url) as url:
        get_movies_data = url.read()
        get_movies_response = json.loads(get_movies_data)

        if get_movies_response['results']:
            movies_result_list = get_movies_response['results']
            movie_results = process_results(movies_result_list)
    return movie_results

def process_results(movie_list):
    """Process the movie review"""
    movie_results = []

    for movie_item in movie_list:
        id = movie_item.get('id')
        title = movie_item.get('original_title')
        overview = movie_item.get('overview')
        poster = movie_item.get('poster_path')
        vote_average = movie_item.get('vote_average')
        vote_count = movie_item.get('vote_count')

        if poster:
            movie_object = Movie(id, title, overview, poster, vote_average, vote_count)
            movie_results.append(movie_object)

    return movie_results
