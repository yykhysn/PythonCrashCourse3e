"""  A number raised to the third power is a cube. Plot the first five cubic 
numbers, and then plot the first 5,000 cubic numbers. """


import matplotlib.pyplot as pyplot


# Plot the first five cubic numbers
input_values = range(1, 5)
cubic_numbers = [x**3 for x in input_values]
fig, ax = pyplot.subplots()
ax.scatter(input_values, cubic_numbers)
pyplot.show()


# Plot the first 5000 cubic numbers
input_values = range(1, 5000)
cubic_numbers = [x**3 for x in input_values]
fig, ax = pyplot.subplots()
ax.scatter(input_values, cubic_numbers)
pyplot.show()
