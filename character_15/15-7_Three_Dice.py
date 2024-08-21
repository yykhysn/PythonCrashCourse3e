""" When you roll three D6 dice, the smallest number you can roll is 3 and the 
largest number is 18. Create a visualization that shows what happens when you 
roll three D6 dice. """


from random import randint
import plotly.express as express
import numpy
from collections import Counter


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

    

# Create three 6-sides dices and roll them 1000 times for each to see what will 
# happen
dice_1, dice_2, dice_3 = Dice(6), Dice(6), Dice(6)
dices = [dice_1, dice_2, dice_3]
result_3_D6 = numpy.add(dice_1.roll_continuous(1000), dice_2.roll_continuous(1000))
result_3_D6 = numpy.add(result_3_D6, dice_3.roll_continuous(1000))
result_3_D6_frequency = Counter(result_3_D6)

#Plot the bar graph
figure = express.bar(x=result_3_D6_frequency.keys(), y=result_3_D6_frequency.values())
figure.update_layout(xaxis_dtick=1)
figure.show()