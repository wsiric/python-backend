# CSV file now act like a database

import pandas as pd
import pycountry
import json
import os

class Population():

    exclude_countries = {"More developed regions", 
                         "Northern America (UN)", 
                         "Oceania (UN)", 
                         "Upper-middle-income countries", 
                         "Lower-middle-income countries", 
                         "Low-income countries", 
                         "Less developed regions, excluding least developed countries",
                         "Less developed regions, excluding China",
                         "Less developed regions",
                         "Least developed countries",
                         "Latin America and the Caribbean (UN)",
                         "Land-locked developing countries (LLDC)",
                         "High-income countries",
                         "Asia (UN)",
                         "Europe (UN)",
                         }

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

                if (country_name not in Population.exclude_countries):
                    db.setdefault(year, []).append((country_name, population))

            for year, data in db.items():
                db[year] = sorted(data, key=lambda x: x[1], reverse=True)
                
            with open("db.json", 'w') as fh:
                json.dump(db, fh)
        except Exception as e:
            print(f"Error: {e}")
