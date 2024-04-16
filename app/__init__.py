import os
from flask import Flask
from flask_cors import CORS
from .extension import api
from .apis import population_api
from .models import Population

def create_app():
    app = Flask(__name__)

    api.init_app(app)

    cur_dir = os.path.dirname(__file__)
    csv_path = os.path.join(cur_dir, 'pop.csv')
    Population.initialize_data(csv_path)

    api.add_namespace(population_api)
    CORS(app, resources={r'/*':{'origins':"*"}})

    return app
