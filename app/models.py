# CSV file now act like a database

import pandas as pd
import pycountry_convert as pc
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
                         "Africa (UN)",
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
                region = Population.country_to_continent(country_name)

                if country_name not in Population.exclude_countries:
                    db.setdefault(region, {}).setdefault(year, []).append((country_name, population))

            # Sort the data by population for each region and year
            for region_data in db.values():
                for year_data in region_data.values():
                    year_data.sort(key=lambda x: x[1], reverse=True)
            
            # Add the sum of population for each year
            for region_data in db.values():
                for year, year_data in region_data.items():
                    population_sum = sum(entry[1] for entry in year_data)
                    year_data.insert(0, ("Total", population_sum))
            
            with open("db.json", 'w') as fh:
                json.dump(db, fh)
        except Exception as e:
            print(f"Error: {e}")

    def country_to_continent(country_name):
        try:
            country_alpha2 = pc.country_name_to_country_alpha2(country_name)
            country_continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
            country_continent_name = pc.convert_continent_code_to_continent_name(country_continent_code)
            return country_continent_name
        except:
            return "Unknown"