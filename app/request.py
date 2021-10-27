from app import app
import urllib.request, json
from .models import movie

Movie = movie.Movie

#Getting API key
api_key = app.config['MOVIE_API_KEY']

#Getting the movie base url
base_url = app.cofig["MOVIE_API_BASE_URL"]

def get_movies(category): #function takes category as an argument
  '''
  Function that gets the json response to our url request
  '''
  get_movies_url = base_url.format(category, api_key)
  with urllib.request.urlopen(get_movies_url) as url:
    get_movies_data = url.read()
    get_movies_response = json.loads(get_movies_data)

    movie_result = None

    if get_movies_response['results']:
      movie_result_list = get_movies_response['result']
      movie_result = process_results(movie_result_list)

  return movie_result