""" Sitka is located in a temperate rainforesst, so it gets a fair amount of 
rainfall. In the data file sitka_weather_2021_full.csv is a header called PRCP, 
which represents daily rainfall amounts. Make a visualization focusing on the 
data in this column. You can repeat the exercise for Death Valley if you’re 
curious how little rainfall occurs in a desert. """


import csv
import matplotlib.pyplot as pyplot


weather_data_file = open('sitka_weather_2021_full.csv')
weather_data_reader = csv.DictReader(weather_data_file)
daily_rainfall_amounts_date, daily_rainfall_amounts, daily_rainfall_date = [], [], []
for row in weather_data_reader:
    daily_rainfall_amounts_date.append({row['DATE']:float(row['PRCP'])})
    daily_rainfall_date.append(row['DATE'])
    daily_rainfall_amounts.append(float(row['PRCP']))
if not len(daily_rainfall_amounts) == len(daily_rainfall_date):
    print("Data Missing")
weather_data_file.close()

fig, ax = pyplot.subplots()
ax.plot(daily_rainfall_date, daily_rainfall_amounts)
fig.autofmt_xdate()
pyplot.show()