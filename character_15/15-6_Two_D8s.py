""" Create a simulation showing what happens when you roll two eight-sided dice 
1,000 times. Try to picture what you think the visualization will look like 
before you run the simulation, then see if your intuition was correct. Gradually 
increase the number of rolls until you start to see the limits of your system’s 
capabilities. """

from random import randint
import plotly.express as express
import numpy
from collections import Counter


class Dice:
    """ A class simulate a dice """
    def __init__(self, side_num) -> None:
        """ Init the dice with sides """
        self.sides = side_num

    def roll(self):
        """ Roll the dice and get a result """
        return randint(1, self.sides)
    
    def roll_continuous(self, rolling_times):
        """ Continuous roll the dice for rolling_times and get the results """
        results = []
        for count in range(0, rolling_times):
            results.append(self.roll())
        return results
    

# Create two 8-sided dices and calculate results of the sum of the two dices of 
# each roll
dice8_1, dice8_2 = Dice(8), Dice(8)
results = numpy.add(dice8_1.roll_continuous(1000), dice8_2.roll_continuous(1000))
result_frequency = Counter(results)

# Plot the bar graph
figure = express.bar(x=result_frequency.keys(), y=result_frequency.values())
figure.update_layout(xaxis_dtick=1)
figure.show()
