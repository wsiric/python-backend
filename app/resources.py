from flask_restx import Resource, Namespace
import json
population_api = Namespace("population")

@population_api.route("/all")
class Population(Resource):
    def get(self):
        fh = open('db.json', 'r')
        db = json.load(fh)
        return db