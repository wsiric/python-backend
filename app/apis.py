from flask_restx import Resource, Namespace
import json
population_api = Namespace("population")

@population_api.route("/asia")
class Population(Resource):
    def get(self):
        with open('db.json', 'r') as fh:
            db = json.load(fh)
        return db["Asia"]

@population_api.route("/europe")
class Population(Resource):
    def get(self):
        with open('db.json', 'r') as fh:
            db = json.load(fh)
        return db["Europe"]
    
@population_api.route("/africa")
class Population(Resource):
    def get(self):
        with open('db.json', 'r') as fh:
            db = json.load(fh)
        return db["Africa"]
    
@population_api.route("/oceania")
class Population(Resource):
    def get(self):
        with open('db.json', 'r') as fh:
            db = json.load(fh)
        return db["Oceania"]
    
@population_api.route("/na")
class Population(Resource):
    def get(self):
        with open('db.json', 'r') as fh:
            db = json.load(fh)
        return db["North America"]
    
@population_api.route("/sa")
class Population(Resource):
    def get(self):
        with open('db.json', 'r') as fh:
            db = json.load(fh)
        return db["South America"]
    
@population_api.route("/years")
class Years(Resource):
    def get(self):
        return list(range(1950, 2021 + 1))