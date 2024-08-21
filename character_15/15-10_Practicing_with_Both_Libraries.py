""" Try using Matplotlib to make a die-rolling visualization, and use Plotly to 
make the visualization for a random walk. (You’ll need to consult the 
documentation for each library to complete this exercise.) """


from random import randint, choice
import matplotlib.pyplot as pyplot
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
        return [self.roll() for count in range(0, rolling_times)]
    
    def set_value(self, values):
        """ Set a value of each side """
        values_length = len(values)
        if values_length == self.sides:
            self.values = values
        elif values_length > self.sides:
            self.values = values[:self.sides]
        else:
            self.values = values + [values[-1]+count-values_length+1 for count 
                                    in range(values_length, self.sides)]


class RandomWalker:
    """ A class to generate random walk choices. Refactor the previous version 
    in 15-3 to simplify the walk function """

    def __init__(self, walk_steps_num, step_max_length) -> None:
        """ Init a walker with total steps and max length of each step """
        self.walk_num = walk_steps_num
        self.walk_path_x = [0]
        self.walk_path_y = [0]
        self.step_max_length = step_max_length

    def walk(self):
        """ Generate a random walk choice """
        self.walk_path_x.append(self.get_step(self.walk_path_x[-1]))
        self.walk_path_y.append(self.get_step(self.walk_path_y[-1]))
        

    def wall_all(self):
        """ Calculate all the walk choice from start to end """
        for walk_count in range(self.walk_num):
            self.walk()

    def get_step(self, current_position):
        """ New method to determine the direction and distance for each step """
        step_increment = choice([-1, 1]) * choice([0, self.step_max_length])
        return current_position + step_increment


# Create a dice and a random walker
dice = Dice(6)
walker = RandomWalker(10000, 6)

# Roll the dice and use Matplotlib to make a visualization
rolling_results = dice.roll_continuous(10000)
rolling_results_with_frequency = Counter(rolling_results)
pyplot.bar(rolling_results_with_frequency.keys(), rolling_results_with_frequency.values())
pyplot.show()

# Walk the walker and use Plotly to make a visualization
walker.wall_all()
figure = express.scatter(walker.walk_path_x, walker.walk_path_y)
figure.show()