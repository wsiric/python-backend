from flask_restx import Resource, Namespace
import json
population_api = Namespace("population")

@population_api.route("/all")
class Population(Resource):
    def get(self):
        with open('db.json', 'r') as fh:
            db = json.load(fh)
        return db
    
@population_api.route("/years")
class Years(Resource):
    def get(self):
        with open('db.json', 'r') as fh:
            db = json.load(fh)
        return list(db.keys())