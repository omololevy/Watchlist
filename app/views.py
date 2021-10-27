#Views
# 
from flask import render_template
from app import app

#render_template is a function


@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    '''
    View movie page function that returns the movie details page and its data.
    '''
    title = 'Home - Welcome to the best Movie Review Website Online'
    
    return render_template('movie.html', id = movie_id)