""" The fill_walk() method is lengthy. Create a new method called get_step() to 
determine the direction and distance for each step, and then calculate the step. 
You should end up with two calls to x_step = self.get_step() 
y_step = self.get_step() This refactoring should reduce the size of fill_walk() 
and make the method easier to read and understand. """


import matplotlib.pyplot as pyplot
from random import choice


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


# Make a random walk choice instance
walker = RandomWalker(5000, 6)
walker.wall_all()

# Plot the path of the random walk choice instance       
fig, ax = pyplot.subplots()
ax.plot(walker.walk_path_x, walker.walk_path_y)
pyplot.show()