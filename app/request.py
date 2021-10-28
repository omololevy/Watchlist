from app import app
import urllib.request,json
from .models import movie

Movie = movie.Movie

#Getting API key
api_key = app.config['MOVIE_API_KEY']

#Getting the movie base url
base_url = app.config["MOVIE_API_BASE_URL"]

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
      movie_result_list = get_movies_response['results']
      movie_result = process_results(movie_result_list)

  return movie_result

def process_results(movie_list):
  '''
  Function that processes the movie result and transform them to a list of Objects.

  Args:
    movie_list: A list of dictionaries that contain movie details

  Returns:
    movie_results: A list of movie objects
  '''
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

  return movie_results
      