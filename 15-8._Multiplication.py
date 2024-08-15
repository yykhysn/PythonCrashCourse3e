"""  When you roll two dice, you usually add the two numbers together to get the 
result. Create a visualization that shows what happens if you multiply these 
numbers by each other instead. """


from random import randint
import numpy
from collections import Counter
import plotly.express as express


class Dice:
    """ A class simulate a dice """
    def __init__(self, side_num) -> None:
        """ Init the dice with sides """
        self.sides = side_num
        self.values = list(range(1, side_num+1))

    def roll(self):
        """ Roll the dice and get a result """
        return randint(1, self.sides)
    
    def roll_continuous(self, rolling_times):
        """ Continuous roll the dice for rolling_times and get the results """
        results = []
        for count in range(0, rolling_times):
            results.append(self.roll())
        return results
    
    def set_value(self, values):
        """ Set a value of each side """
        if len(values) == self.sides:
            self.values = values
        elif len(values) > self.sides:
            self.values = values[:self.sides]
        else:
            self.values = values
            for count in range(0, len(values)):
                self.values.append(self.values[-1] + 1)


# Create two dices
dice_D6_1, dice_D6_2 = Dice(6), Dice(6)

# Roll the two dices and calculate the product of each roll respectively
results_2D6_product = numpy.multiply(dice_D6_1.roll_continuous(1000), 
                                 dice_D6_2.roll_continuous(1000))
results_2D6_product_frequency = Counter(results_2D6_product)

# Plot the bar
figure = express.bar(x=results_2D6_product_frequency.keys(), 
                      y=results_2D6_product_frequency.values())
figure.show()