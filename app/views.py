from flask import render_template
from app import app
#Views
#render_template is a function


@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')