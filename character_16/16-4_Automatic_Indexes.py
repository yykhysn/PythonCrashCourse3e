""" In this section, we hardcoded the indexes corresponding to the TMIN and TMAX 
columns. Use the header row to determine the indexes for these values, so your 
program can work for Sitka or Death Valley. Use the station name to 
automatically generate an appropriate title for your graph as well. """

import csv
import matplotlib.pyplot as pyplot


weather_data_file = open('sitka_weather_2021_full.csv')
weather_data_reader = csv.DictReader(weather_data_file)
daily_rainfall_amounts_date, daily_rainfall_amounts, daily_rainfall_date = [], [], []
for row in weather_data_reader:
    daily_rainfall_amounts_date.append({row['DATE']:float(row['PRCP'])})
    daily_rainfall_date.append(row['DATE'])
    daily_rainfall_amounts.append(float(row['PRCP']))
    station_name = row["STATION"]
if not len(daily_rainfall_amounts) == len(daily_rainfall_date):
    print("Data Missing")
weather_data_file.close()

fig, ax = pyplot.subplots()
ax.plot(daily_rainfall_date, daily_rainfall_amounts)
fig.autofmt_xdate()
ax.set_title("Daily Rainfall Amounts of Station " + station_name)
pyplot.show()