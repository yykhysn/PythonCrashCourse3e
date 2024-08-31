""" In this section, we used the generic title Global Earthquakes. Instead, you 
can use the title for the dataset in the metadata part of the GeoJSON file. Pull 
this value and assign it to the variable title. """


import json


with open('eq_data_1_day_m1.geojson') as earthquake_record_file:
    original_earthquake_record_data = json.load(earthquake_record_file)
    earthquake_record_metadata = original_earthquake_record_data['metadata']
    earthquake_record_data = original_earthquake_record_data['features']
earthquake_record_longitudes, earthquake_record_latitudes, \
    earthquake_record_titles, earthquake_record_magnitudes = [], [], [], []
for earthquake_record in earthquake_record_data:
    earthquake_record_longitudes.append(earthquake_record['geometry']['coordinates'][0])
    earthquake_record_latitudes.append(earthquake_record['geometry']['coordinates'][1])
    earthquake_record_titles.append(earthquake_record['properties']['title'])
    earthquake_record_magnitudes.append(earthquake_record['properties']['mag'])
title = earthquake_record_metadata['title']