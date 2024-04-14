# CSV file now act like a database

import pandas as pd
import json

class Population():
    def initialize_data(csv_file):
        df = pd.read_csv(csv_file, usecols=['Country name', 'Year', 'Population'])
        db = {}
        for index, row in df.iterrows():
            country_name = row['Country name']
            year = row['Year']
            population = row['Population']
            db.setdefault(year, []).append((country_name, population))
        fh = open("db.json", 'w')
        json.dump(db, fh)