# CSV file now act like a database

import pandas as pd
import json
import os

class Population():
    def initialize_data(csv_file):
        if os.path.exists("db.json"):
            print("Database file already exists. Skipping initialization.")
            return
        
        try:
            df = pd.read_csv(csv_file, usecols=['Country name', 'Year', 'Population'])
            db = {}
            for index, row in df.iterrows():
                country_name = row['Country name']
                year = row['Year']
                population = row['Population']
                db.setdefault(year, []).append((country_name, population))
            with open("db.json", 'w') as fh:
                json.dump(db, fh)
        except Exception as e:
            print(f"Error: {e}")
