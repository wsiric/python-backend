import os
from flask import Flask
from flask_cors import CORS
from apis import population_api
from models import Population
from flask_restx import Api

app = Flask(__name__)

api = Api()
api.init_app(app)

cur_dir = os.path.dirname(__file__)
csv_path = os.path.join(cur_dir, 'pop.csv')
Population.initialize_data(csv_path)

api.add_namespace(population_api)
CORS(app, resources={r'/*':{'origins':"*"}})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(8080))