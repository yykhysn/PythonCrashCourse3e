""" In the resources for this chapter, you’ll find a file called 
world_fires_1_day.csv. This file contains information about fires burning in 
different locations around the globe, including the latitude, longitude, and 
brightness of each fire. Using the data-processing work from the first part of 
this chapter and the mapping work from this section, make a map that shows which 
parts of the world are affected by fires. You can download more recent versions 
of this data at 
https://earthdata.na sa.gov/earth-observation-data/near-real-time/firms/active-fire-data.
You can find links to the data in CSV format in the SHP, KML, and TXT Files 
section. """


import csv
import plotly.express as express


with open("world_fires_1_day.csv") as fires_record_file:
    fires_records = csv.DictReader(fires_record_file)
    fire_latitudes, fire_longitudes, fire_brightnesses_approximately = [], [], []
    for fires_record in fires_records:
        fire_latitudes.append(fires_record['latitude'])
        fire_longitudes.append(fires_record['longitude'])
        fire_brightnesses_approximately.append(float(fires_record['brightness']))

figure = express.scatter_geo(lat=fire_latitudes, lon=fire_longitudes,
                             size=fire_brightnesses_approximately)
figure.show()