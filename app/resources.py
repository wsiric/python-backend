from flask_restx import Resource, Namespace
import json
population_api = Namespace("population")

@population_api.route("/hello")
class Population(Resource):
    def get(self):
        fh = open('db.json', 'r')
        db = json.load(fh)
        res = sorted(db["1950"], key=lambda x: x[1], reverse=True)
        return res