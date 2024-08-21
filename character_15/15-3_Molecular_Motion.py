""" Modify rw_visual.py by replacing ax.scatter() with ax.plot(). To simulate 
the path of a pollen grain on the surface of a drop of water, pass in the 
rw.x_values and rw.y_values, and include a linewidth argument. Use 5,000 
instead of 50,000 points to keep the plot from being too busy. """


import matplotlib.pyplot as pyplot
from random import choice


class RandomWalker:
    """ A class to generate random walk choices """

    def __init__(self, walk_steps_num, step_max_length) -> None:
        """ Init a walker with total steps and max length of each step """
        self.walk_num = walk_steps_num
        self.walk_path_x = [0]
        self.walk_path_y = [0]
        self.step_max_length = step_max_length

    def walk(self):
        """ Generate a random walk choice """
        previous_walk_position_x = self.walk_path_x[-1]
        previous_walk_position_y = self.walk_path_y[-1]
        current_walk_increment_x = choice([-1, 1]) * choice([0, self.step_max_length])
        current_walk_increment_y = choice([-1, 1]) * choice([0, self.step_max_length])
        self.walk_path_x.append(previous_walk_position_x + current_walk_increment_x)
        self.walk_path_y.append(previous_walk_position_y + current_walk_increment_y)

    def wall_all(self):
        """ Calculate all the walk choice from start to end """
        for walk_count in range(self.walk_num):
            self.walk()


# Make a random walk choice instance
walker = RandomWalker(5000, 6)
walker.wall_all()

# Plot the path of the random walk choice instance       
fig, ax = pyplot.subplots()
ax.plot(walker.walk_path_x, walker.walk_path_y)
pyplot.show()