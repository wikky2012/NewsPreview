from flask import render_template
from .request import get_news
from app import app

# @app.route('/')
# def index():

#     popular_news = get_news('popular')
#     print(popular_news)
#     title = 'Home - Welcome to The best News Preview Website Online'
#     return render_template('index.html', title = title,popular = popular_news)

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular news
    trending_news = get_news('trending')
    
    title = 'Home - Welcome to The best News Preview Website Online'
    return render_template('index.html', title = title, trending = trending_news)