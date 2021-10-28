#Views
# 
from flask import render_template
from app import app
from .request import get_movies
#render_template is a function


@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    '''
    View movie page function that returns the movie details page and its data.
    '''
    title = 'Home - Welcome to the best Movie Review Website Online'
    
    return render_template('movie.html', id = movie_id)

@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    #Getting popular movies
    popular_movies = get_movies('popular')
    print(popular_movies)
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title = title, popular = popular_movies)
