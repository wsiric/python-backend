from flask import Flask
from .extension import api
from .resources import population_api
from .models import Population

def create_app():
    app = Flask(__name__)

    api.init_app(app)
    Population.initialize_data('C:\\Users\\Witsa\\Desktop\\job\\python-backend\\app\\pop.csv')

    api.add_namespace(population_api)

    return app
