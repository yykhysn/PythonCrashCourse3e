""" The loop that pulls data from all_eq_dicts uses variables for the magnitude, 
longitude, latitude, and title of each earthquake before appending these values 
to their appropriate lists. This approach was chosen for clarity in how to pull 
data from a GeoJSON file, but it’s not necessary in your code. Instead of using 
these temporary variables, pull each value from eq_dict and append it to the 
appropriate list in one line. Doing so should shorten the body of this loop to 
just four lines. """


import json


with open('eq_data_1_day_m1.geojson') as earthquake_record_file:
    earthquake_record_data = json.load(earthquake_record_file)['features']
earthquake_record_longitudes, earthquake_record_latitudes, \
    earthquake_record_titles, earthquake_record_magnitudes = [], [], [], []
for earthquake_record in earthquake_record_data:
    earthquake_record_longitudes.append(earthquake_record['geometry']['coordinates'][0])
    earthquake_record_latitudes.append(earthquake_record['geometry']['coordinates'][1])
    earthquake_record_titles.append(earthquake_record['properties']['title'])
    earthquake_record_magnitudes.append(earthquake_record['properties']['mag'])