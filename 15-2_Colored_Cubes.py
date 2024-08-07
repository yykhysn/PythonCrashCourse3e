"""  Apply a colormap to your cubes plot. """


import matplotlib.pyplot as pyplot


input_values = range(1, 5000)
cubic_numbers = [x**3 for x in input_values]
fig, ax = pyplot.subplots()
ax.scatter(input_values, cubic_numbers, c=cubic_numbers, cmap=pyplot.cm.Blues)
pyplot.show()