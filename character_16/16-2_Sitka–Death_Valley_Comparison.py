""" The temperature scales on the Sitka and Death Valley graphs reflect the 
different data ranges. To accurately compare the temperature range in Sitka to 
that of Death Valley, you need identical scales on the y-axis. Change the 
settings for the y-axis on one or both of the charts in Figures 16-5 and 16-6. 
Then make a direct comparison between temperature ranges in Sitka and Death 
Valley (or any two places you want to compare). """


import csv
import matplotlib.pyplot as pyplot


sitka_weather_file = open("sitka_weather_2021_simple.csv")
death_valley_weather_file = open("death_valley_2021_simple.csv")
sitka_weather_reader = csv.DictReader(sitka_weather_file)
death_valley_weather_reader = csv.DictReader(death_valley_weather_file)
sitka_min_temperatures = []
sitka_max_temperatures = []
sitka_record_dates = []
for record in sitka_weather_reader:
    sitka_min_temperatures.append(record['TMIN'])
    sitka_max_temperatures.append(record['TMAX'])
    sitka_record_dates.append(record['DATE'])
death_valley_min_temperatures = []
death_valley_max_temperatures = []
death_valley_record_dates = []
for record in death_valley_weather_reader:
    death_valley_min_temperatures.append(record['TMIN'])
    death_valley_max_temperatures.append(record['TMAX'])
    death_valley_record_dates.append(record['DATE'])
sitka_weather_file.close()
death_valley_weather_file.close()

fig1, ax1 = pyplot.subplots()
ax1.plot(sitka_record_dates, sitka_max_temperatures, color='red', alpha=0.5)
ax1.plot(sitka_record_dates, sitka_min_temperatures, color='blue', alpha=0.5)
ax1.fill_between(sitka_record_dates, sitka_max_temperatures, sitka_min_temperatures,
                 alpha=0.3, facecolor='grey')
fig2, ax2 = pyplot.subplots()
ax2.plot(death_valley_record_dates, death_valley_max_temperatures, color='red', alpha=0.5)
ax2.plot(death_valley_record_dates, death_valley_min_temperatures, color='blue', alpha=0.5)
ax2.fill_between(death_valley_record_dates, death_valley_min_temperatures, 
                 death_valley_max_temperatures, alpha=0.3, facecolor='grey')

pyplot.ylim(0, 100)
pyplot.show()