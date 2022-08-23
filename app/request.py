from flask import current_app

import json, urllib.request, requests

from .models import Movie

# def get_movies(category):
#     # current_app.config.get()
#     base_url = current_app.config.get('MOVIE_API_BASE_URL')
#     get_movies_url = f"{base_url}/{category}{current_app.config.get('MOVIE_API_PAYLOAD')}"
    
    
#     movie_results = None
#     # print(get_movies_url)
#     # get_movies_data = requests.get(get_movies_url)
#     with urllib.request.urlopen(get_movies_url) as url:
#         get_movies_data = url.read()
#         get_movies_response = json.loads(get_movies_data)

#         if get_movies_response['results']:
#             movies_result_list = get_movies_response['results']
#             movie_results = process_results(movies_result_list)
#     return movie_results

def get_movies(category):
    """Get movies by category"""
    # configure url
    base_url = current_app.config.get('MOVIE_API_BASE_URL')
    movies_url = f"{base_url}/{category}{current_app.config.get('MOVIE_API_PAYLOAD')}"
    print(movies_url)

    # fetch from movies url
    movies_response = requests.get(movies_url).text
    # print(movies_response)

    # parse movie response to dict items
    movies = json.loads(movies_response).get('results')
    # print(movies)

    # get uniform movie items as processed with Movie class
    return process_results(movies)
    

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

def get_movie(id):
    base_url = current_app.config.get('MOVIE_API_BASE_URL') + f'/{id}'
    get_movie_details_url = f"{current_app.config.get('MOVIE_API_BASE_URL') + f'/{id}'}{current_app.config.get('MOVIE_API_PAYLOAD')}"
    print(get_movie_details_url)

    movie_object = None
    with urllib.request.urlopen(get_movie_details_url) as url:
        movie_details_data = url.read()
        movie_details_response = json.loads(movie_details_data)

        if movie_details_response:
            id = movie_details_response.get('id')
            title = movie_details_response.get('original_title')
            overview = movie_details_response.get('overview')
            poster = movie_details_response.get('poster_path')
            vote_average = movie_details_response.get('vote_average')
            vote_count = movie_details_response.get('vote_count')

            movie_object = Movie(id, title, overview, poster, vote_average, vote_count)

    return movie_object

