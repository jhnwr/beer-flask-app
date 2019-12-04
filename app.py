from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import requests
import json

APP = Flask(__name__)

@APP.route('/')
def index():
    #url = f'https://api.punkapi.com/v2/beers/{}'

    beer_data = []
    
    r = requests.get(f'https://api.punkapi.com/v2/beers/random')

    random_beer = json.loads(r.text)

    beer = {
        'name': random_beer[0]['name'], 
        'tag': random_beer[0]['tagline'],
        'desc': random_beer[0]['description'], 
        'abv': random_beer[0]['abv'], 
        'img': random_beer[0]['image_url']
        }

    beer_data.append(beer)
    print(beer_data)

    
    return render_template('main.html', beer=beer)

if __name__ == '__main__':
    APP.debug=True
    APP.run()
